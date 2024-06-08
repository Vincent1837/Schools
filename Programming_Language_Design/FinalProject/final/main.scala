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