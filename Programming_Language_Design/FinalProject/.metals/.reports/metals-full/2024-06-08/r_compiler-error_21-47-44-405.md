file://<WORKSPACE>/final/main.scala
### java.lang.AssertionError: assertion failed: denotation class Object invalid in run 4. ValidFor: Period(1..2, run = 5)

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.3
Classpath:
<HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.3/scala3-library_3-3.3.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.12/scala-library-2.13.12.jar [exists ]
Options:



action parameters:
uri: file://<WORKSPACE>/final/main.scala
text:
```scala
import scala.collection.immutable.Map
import scala.util.{Try, Success, Failure}

object JDoodle {

  case class User(name: String, ownedSheets: Set[String] = Set(), sharedSheets: Set[String] = Set())

  case class Sheet(name: String, data: Array[Array[Double]], accessRight: String, owner: String, collaborators: Set[String])

  type Users = Map[String, User]
  type Sheets = Map[String, Sheet]

  trait AccessControl {
    def accessEnabled: Boolean
    def editable(sheet: Sheet): Boolean
  }

  object NoAccessControl extends AccessControl {
    override def accessEnabled: Boolean = false
    override def editable(sheet: Sheet): Boolean = true
  }

  object EnableAccessControl extends AccessControl {
    override def accessEnabled: Boolean = true
    override def editable(sheet: Sheet): Boolean =
      sheet.accessRight == "editable"
  }

  trait SharingControl {
    def sharingEnabled: Boolean
    def hasAccess(sheet: Sheet, userName: String): Boolean
  }

  object NoSharingControl extends SharingControl {
    override def sharingEnabled: Boolean = false
    override def hasAccess(sheet: Sheet, userName: String): Boolean = sheet.owner == userName
  }

  object EnableSharingControl extends SharingControl {
    override def sharingEnabled: Boolean = true
    override def hasAccess(sheet: Sheet, userName: String): Boolean =
      sheet.owner == userName || sheet.collaborators.contains(userName)
  }

  def createUser(users: Users, name: String): Either[String, Users] = {
    if (users.contains(name)) {
      Left(s"User '$name' already exists.")
    } else {
      Right(users + (name -> User(name)))
    }
  }

  def createSheet(users: Users, sheets: Sheets, userName: String, sheetName: String): Either[String, (Users, Sheets)] = {
    if (!users.contains(userName)) {
      Left(s"User '$userName' does not exist.")
    } else {
      val user = users(userName)
      if (user.ownedSheets.contains(sheetName) || user.sharedSheets.contains(sheetName)) {
        Left(s"Sheet '$sheetName' already exists for user '$userName'.")
      } else {
        val newUser = user.copy(ownedSheets = user.ownedSheets + sheetName)
        val newSheet = Sheet(sheetName, Array.fill(3, 3)(0.0), "editable", userName, Set())
        Right(users + (userName -> newUser), sheets + (sheetName -> newSheet))
      }
    }
  }

  def checkSheet(users: Users, sheets: Sheets, sheetName: String, userName: String, accessControl: AccessControl, sharingControl: SharingControl): Either[String, Array[Array[Double]]] = {
    if (!users.contains(userName)) {
        return Left(s"User '$userName' does not exist.")
    }
    sheets.get(sheetName).map { sheet =>
      if (sharingControl.hasAccess(sheet, userName)) Right(sheet.data)
      else Left("This sheet is not accessible.")
    }.getOrElse(Left("Sheet not found."))
  }

  def changeValue(users: Users, sheets: Sheets, userName: String, sheetName: String, row: Int, col: Int, value: String, accessControl: AccessControl, sharingControl: SharingControl): Either[String, Sheets] = {
    if (!users.contains(userName)) {
        return Left(s"User '$userName' does not exist.")
    }

    sheets.get(sheetName).map { sheet =>
        if (sharingControl.hasAccess(sheet, userName)) {
        if (accessControl.editable(sheet)) {
            Try(evaluate(value)) match {
            case Success(newValue) =>
                val newData = sheet.data.updated(row, sheet.data(row).updated(col, newValue))
                Right(sheets + (sheetName -> sheet.copy(data = newData)))
            case Failure(_) => Left("Invalid value. Unable to evaluate the expression.")
            }
        } else {
            Left("This sheet is readonly.")
        }
        } else {
        Left("This sheet is not accessible.")
        }
    }.getOrElse(Left("Sheet not found."))
    }



  def changeAccessRight(users: Users, sheets: Sheets, username: String, sheetName: String, right: String, accessControl: AccessControl): Either[String, Sheets] = {
    if (!accessControl.accessEnabled) {
        Left("Access control is not enabled.")
    } else if (!users.contains(username)) {
        Left(s"User '$username' does not exist.")
    } else {
        sheets.get(sheetName).map { sheet =>
        if (sheet.owner != username) {
            Left("Only the owner can change the access right.")
        } else if (right != "readonly" && right != "editable") {
            Left("Invalid access right.")
        } else {
            val newSheet = sheet.copy(accessRight = right)
            Right(sheets + (sheetName -> newSheet))
        }
        }.getOrElse(Left("Sheet not found."))
    }
  }

  def shareSheet(users: Users, sheets: Sheets, sheetName: String, ownerName: String, collaboratorName: String, sharingControl: SharingControl): Either[String, (Users, Sheets)] = {
    if (!sharingControl.sharingEnabled) {
        return Left("Sharing is not enabled.")
    }
    if (!users.contains(ownerName)) {
        return Left(s"User '$ownerName' does not exist.")
    }
    if (!users.contains(collaboratorName)) {
        return Left(s"User '$collaboratorName' does not exist.")
    }

    sheets.get(sheetName).map { sheet =>
        if (sheet.owner != ownerName) {
        Left("Only the owner can share the sheet.")
        } else if (users(collaboratorName).ownedSheets.contains(sheetName) || users(collaboratorName).sharedSheets.contains(sheetName)) {
        Left(s"User '$collaboratorName' already owns a sheet with the same name.")
        } else {
        val newUser = users(collaboratorName).copy(sharedSheets = users(collaboratorName).sharedSheets + sheetName)
        val newSheet = sheet.copy(collaborators = sheet.collaborators + collaboratorName)
        Right(users + (collaboratorName -> newUser), sheets + (sheetName -> newSheet))
        }
    }.getOrElse(Left("Sheet not found."))
  }

  def evaluate(expression: String): Double = {
    val trimmedExpression = expression.trim
    if (trimmedExpression.forall(c => c.isDigit || c == '.')) {
        return trimmedExpression.toDouble
    }
    val operatorPattern = "([+\\-*/])".r
    val parts = operatorPattern.split(trimmedExpression).map(_.trim)
    val operator = operatorPattern.findFirstIn(trimmedExpression).get
    val left = parts(0).toDouble
    val right = parts(1).toDouble
    operator match {
        case "+" => left + right
        case "-" => left - right
        case "*" => left * right
        case "/" => left / right
    }
  }

  def mainMenu(users: Users, sheets: Sheets, accessControl: AccessControl, sharingControl: SharingControl): (Users, Sheets) = {
    println("---------------Menu---------------")
    println("1. Create a user")
    println("2. Create a sheet")
    println("3. Check a sheet")
    println("4. Change a value in a sheet")
    println("5. Change a sheet's access right")
    println("6. Collaborate with another user")
    println("0. Exit")
    println("----------------------------------")
    print("> ")

    val choice = scala.io.StdIn.readLine()

    val (updatedUsers, updatedSheets) = choice match {
        case "1" =>
        print("Enter username: ")
        val name = scala.io.StdIn.readLine()
        createUser(users, name) match {
            case Right(newUsers) => (newUsers, sheets)
            case Left(error) =>
            println(error)
            (users, sheets)
        }
        case "2" =>
        print("Enter username, sheet name: ")
        val Array(userName, sheetName) = scala.io.StdIn.readLine().split(" ")
        createSheet(users, sheets, userName, sheetName) match {
            case Right((newUsers, newSheets)) => (newUsers, newSheets)
            case Left(error) =>
            println(error)
            (users, sheets)
        }
        case "3" =>
        print("Enter username, sheet name: ")
        val Array(userName, sheetName) = scala.io.StdIn.readLine().split(" ")
        checkSheet(users, sheets, sheetName, userName, accessControl, sharingControl) match {
            case Right(data) => data.foreach(row => println(row.mkString(", ")))
            case Left(error) => println(error)
        }
        (users, sheets)
        case "4" =>
        print("Enter username, sheet name: ")
        val Array(userName, sheetName) = scala.io.StdIn.readLine().split(" ")
        checkSheet(users, sheets, sheetName, userName, accessControl, sharingControl) match {
            case Right(data) => data.foreach(row => println(row.mkString(", ")))
            case Left(error) => println(error)
        }
        print("Enter row, col, value: ")
        val Array(row, col, value) = scala.io.StdIn.readLine().split(" ")
        changeValue(users, sheets, userName, sheetName, row.toInt, col.toInt, value, accessControl, sharingControl) match {
            case Right(newSheets) =>
            checkSheet(users, newSheets, sheetName, userName, accessControl, sharingControl) match {
                case Right(data) => data.foreach(row => println(row.mkString(", ")))
                case Left(error) => println(error)
            }
            (users, newSheets)
            case Left(error) =>
            println(error)
            (users, sheets)
        }
        case "5" =>
        print("Enter username, sheet name and new access right(readonly/editable): ")
        val Array(username, sheetName, right) = scala.io.StdIn.readLine().split(" ")
        changeAccessRight(users, sheets, username, sheetName, right, accessControl) match {
            case Right(newSheets) => 
                println(s"User '$username' changed the access right of sheet '$sheetName' to '$right'.")
                (users, newSheets)
            case Left(error) =>
            println(error)
            (users, sheets)
        }
        case "6" =>
        print("Enter sheet name, owner name and collaborator name: ")
        val Array(sheetName, ownerName, collaboratorName) = scala.io.StdIn.readLine().split(" ")
        shareSheet(users, sheets, sheetName, ownerName, collaboratorName, sharingControl) match {
            case Right((newUsers, newSheets)) => 
                println(s"User '$ownerName' shared sheet '$sheetName' with user '$collaboratorName'.")
                (newUsers, newSheets)
            case Left(error) =>
            println(error)
            (users, sheets)
        }
        case "0" =>
            println("Exiting...")
            return (users, sheets)
        case _ =>
        println("Invalid option, please try again.")
        (users, sheets)
    }
    println()
    mainMenu(updatedUsers, updatedSheets, accessControl, sharingControl)
  }

  def main(args: Array[String]): Unit = {
    var users: Users = Map()
    var sheets: Sheets = Map()
    val accessControl = EnableAccessControl
    val sharingControl = EnableSharingControl
  
    mainMenu(users, sheets, accessControl, sharingControl)
  }
}
```



#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:8)
	dotty.tools.dotc.core.Denotations$SingleDenotation.updateValidity(Denotations.scala:717)
	dotty.tools.dotc.core.Denotations$SingleDenotation.bringForward(Denotations.scala:742)
	dotty.tools.dotc.core.Denotations$SingleDenotation.toNewRun$1(Denotations.scala:799)
	dotty.tools.dotc.core.Denotations$SingleDenotation.current(Denotations.scala:870)
	dotty.tools.dotc.core.Symbols$Symbol.recomputeDenot(Symbols.scala:120)
	dotty.tools.dotc.core.Symbols$Symbol.computeDenot(Symbols.scala:114)
	dotty.tools.dotc.core.Symbols$Symbol.denot(Symbols.scala:107)
	dotty.tools.dotc.core.Symbols$.toDenot(Symbols.scala:494)
	dotty.tools.dotc.core.Denotations$SingleDenotation.updateValidity(Denotations.scala:716)
	dotty.tools.dotc.core.Denotations$SingleDenotation.bringForward(Denotations.scala:742)
	dotty.tools.dotc.core.Denotations$SingleDenotation.toNewRun$1(Denotations.scala:799)
	dotty.tools.dotc.core.Denotations$SingleDenotation.current(Denotations.scala:870)
	dotty.tools.dotc.core.Types$NamedType.computeDenot(Types.scala:2391)
	dotty.tools.dotc.core.Types$NamedType.denot(Types.scala:2351)
	dotty.tools.dotc.core.Types$NamedType.info(Types.scala:2340)
	dotty.tools.dotc.core.TypeApplications$.hkResult$extension(TypeApplications.scala:260)
	dotty.tools.dotc.core.TypeApplications$.isLambdaSub$extension(TypeApplications.scala:232)
	dotty.tools.dotc.core.TypeComparer.glb(TypeComparer.scala:2231)
	dotty.tools.dotc.core.TypeComparer$.glb(TypeComparer.scala:2985)
	dotty.tools.dotc.core.TypeComparer$.glb$$anonfun$1(TypeComparer.scala:2989)
	scala.collection.LinearSeqOps.foldLeft(LinearSeq.scala:183)
	scala.collection.LinearSeqOps.foldLeft$(LinearSeq.scala:179)
	scala.collection.immutable.List.foldLeft(List.scala:79)
	dotty.tools.dotc.core.TypeComparer$.glb(TypeComparer.scala:2989)
	dotty.tools.dotc.typer.Namer.ensureFirstIsClass(Namer.scala:460)
	dotty.tools.dotc.typer.Namer$ClassCompleter.completeInCreationContext(Namer.scala:1595)
	dotty.tools.dotc.typer.Namer$Completer.complete(Namer.scala:814)
	dotty.tools.dotc.core.SymDenotations$SymDenotation.completeFrom(SymDenotations.scala:174)
	dotty.tools.dotc.core.Denotations$Denotation.completeInfo$1(Denotations.scala:187)
	dotty.tools.dotc.core.Denotations$Denotation.info(Denotations.scala:189)
	dotty.tools.dotc.core.SymDenotations$ClassDenotation.computeMembersNamed(SymDenotations.scala:2145)
	dotty.tools.dotc.core.SymDenotations$ClassDenotation.membersNamed(SymDenotations.scala:2115)
	dotty.tools.dotc.core.SymDenotations$ClassDenotation.findMember(SymDenotations.scala:2166)
	dotty.tools.dotc.core.Types$Type.go$1(Types.scala:721)
	dotty.tools.dotc.core.Types$Type.findMember(Types.scala:900)
	dotty.tools.dotc.typer.TypeAssigner.selectionType(TypeAssigner.scala:155)
	dotty.tools.dotc.typer.TypeAssigner.selectionType$(TypeAssigner.scala:16)
	dotty.tools.dotc.typer.Typer.selectionType(Typer.scala:117)
	dotty.tools.dotc.typer.Typer.typedSelect(Typer.scala:682)
	dotty.tools.dotc.typer.Typer.typeSelectOnTerm$1(Typer.scala:756)
	dotty.tools.dotc.typer.Typer.typedSelect(Typer.scala:793)
	dotty.tools.dotc.typer.Typer.typedNamed$1(Typer.scala:3019)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3114)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3187)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3191)
	dotty.tools.dotc.typer.Typer.typedExpr(Typer.scala:3303)
	dotty.tools.dotc.typer.Applications.realApply$1(Applications.scala:941)
	dotty.tools.dotc.typer.Applications.typedApply(Applications.scala:1101)
	dotty.tools.dotc.typer.Applications.typedApply$(Applications.scala:352)
	dotty.tools.dotc.typer.Typer.typedApply(Typer.scala:117)
	dotty.tools.dotc.typer.Typer.typedUnnamed$1(Typer.scala:3050)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3115)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3187)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3191)
	dotty.tools.dotc.typer.Typer.typedExpr(Typer.scala:3303)
	dotty.tools.dotc.typer.Typer.typedValDef(Typer.scala:2424)
	dotty.tools.dotc.typer.Typer.typedNamed$1(Typer.scala:3023)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3114)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3187)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3191)
	dotty.tools.dotc.typer.Typer.traverse$1(Typer.scala:3213)
	dotty.tools.dotc.typer.Typer.typedStats(Typer.scala:3259)
	dotty.tools.dotc.typer.Typer.typedPackageDef(Typer.scala:2812)
	dotty.tools.dotc.typer.Typer.typedUnnamed$1(Typer.scala:3083)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3115)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3187)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3191)
	dotty.tools.dotc.typer.Typer.typedExpr(Typer.scala:3303)
	dotty.tools.dotc.typer.TyperPhase.typeCheck$$anonfun$1(TyperPhase.scala:44)
	dotty.tools.dotc.typer.TyperPhase.typeCheck$$anonfun$adapted$1(TyperPhase.scala:50)
	scala.Function0.apply$mcV$sp(Function0.scala:42)
	dotty.tools.dotc.core.Phases$Phase.monitor(Phases.scala:440)
	dotty.tools.dotc.typer.TyperPhase.typeCheck(TyperPhase.scala:50)
	dotty.tools.dotc.typer.TyperPhase.runOn$$anonfun$3(TyperPhase.scala:84)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.immutable.List.foreach(List.scala:333)
	dotty.tools.dotc.typer.TyperPhase.runOn(TyperPhase.scala:84)
	dotty.tools.dotc.Run.runPhases$1$$anonfun$1(Run.scala:246)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.ArrayOps$.foreach$extension(ArrayOps.scala:1323)
	dotty.tools.dotc.Run.runPhases$1(Run.scala:262)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1(Run.scala:270)
	dotty.tools.dotc.Run.compileUnits$$anonfun$adapted$1(Run.scala:279)
	dotty.tools.dotc.util.Stats$.maybeMonitored(Stats.scala:71)
	dotty.tools.dotc.Run.compileUnits(Run.scala:279)
	dotty.tools.dotc.Run.compileSources(Run.scala:194)
	dotty.tools.dotc.interactive.InteractiveDriver.run(InteractiveDriver.scala:165)
	scala.meta.internal.pc.MetalsDriver.run(MetalsDriver.scala:45)
	scala.meta.internal.pc.PcCollector.<init>(PcCollector.scala:44)
	scala.meta.internal.pc.PcSemanticTokensProvider$Collector$.<init>(PcSemanticTokensProvider.scala:61)
	scala.meta.internal.pc.PcSemanticTokensProvider.Collector$lzyINIT1(PcSemanticTokensProvider.scala:61)
	scala.meta.internal.pc.PcSemanticTokensProvider.Collector(PcSemanticTokensProvider.scala:61)
	scala.meta.internal.pc.PcSemanticTokensProvider.provide(PcSemanticTokensProvider.scala:90)
	scala.meta.internal.pc.ScalaPresentationCompiler.semanticTokens$$anonfun$1(ScalaPresentationCompiler.scala:110)
```
#### Short summary: 

java.lang.AssertionError: assertion failed: denotation class Object invalid in run 4. ValidFor: Period(1..2, run = 5)