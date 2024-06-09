import scala.collection.immutable.Map
import scala.util.{Try, Success, Failure}

object CollaborativeSheet {

  case class User(name: String)
  case class Sheet(name: String, data: Array[Array[Double]], accessRight: String, owner: String, collaborators: Set[String])

  type Users = Map[String, User]
  type Sheets = Map[String, Sheet]

  // Trait and objects for access control
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
    override def editable(sheet: Sheet): Boolean = sheet.accessRight == "editable"
  }

  // Trait and objects for sharing control
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

  // Function to create a new user
  def createUser(users: Users, name: String): Either[String, Users] = {
    if (users.contains(name)) {
      Left(s"User '$name' already exists.")
    } else {
      Right(users + (name -> User(name)))
    }
  }

  // Function to create a new sheet
  def createSheet(users: Users, sheets: Sheets, userName: String, sheetName: String): Either[String, Sheets] = {
    if (sheets.contains(sheetName)) {
      Left(s"Sheet '$sheetName' already exists.")
    } else if (!users.contains(userName)) {
      Left(s"User '$userName' does not exist.")
    } else {
      val newSheet = Sheet(sheetName, Array.fill(3, 3)(0.0), "editable", userName, Set())
      Right(sheets + (sheetName -> newSheet))
    }
  }

  // Function to check a sheet's data
  def checkSheet(users: Users, sheets: Sheets, sheetName: String, userName: String, accessControl: AccessControl, sharingControl: SharingControl): Either[String, Array[Array[Double]]] = {
    if (!users.contains(userName)) {
      return Left(s"User '$userName' does not exist.")
    }
    sheets.get(sheetName).map { sheet =>
      if (sharingControl.hasAccess(sheet, userName)) Right(sheet.data)
      else Left("This sheet is not accessible.")
    }.getOrElse(Left("Sheet not found."))
  }

  // Function to change a cell value in a sheet
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

  // Function to change access rights of a sheet
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

  // Function to share a sheet with another user
  def shareSheet(users: Users, sheets: Sheets, ownerName: String, sheetName: String, collaboratorName: String, sharingControl: SharingControl): Either[String, Sheets] = {
    if (!sharingControl.sharingEnabled) {
      Left("Sharing is not enabled.")
    } else if (!users.contains(ownerName)) {
      Left(s"User '$ownerName' does not exist.")
    } else if (!users.contains(collaboratorName)) {
      Left(s"User '$collaboratorName' does not exist.")
    } else {
      sheets.get(sheetName).map { sheet =>
        if (sheet.owner == ownerName) {
          Right(sheets + (sheetName -> sheet.copy(collaborators = sheet.collaborators + collaboratorName)))
        } else {
          Left("Only the owner can share the sheet.")
        }
      }.getOrElse(Left("Sheet not found."))
    }
  }

  // Function to evaluate an expression
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

  // Main menu to interact with the system
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
          case Right(newUsers) =>
            println(s"Created a user named '$name'.")
            (newUsers, sheets)
          case Left(error) =>
            println(error)
            (users, sheets)
        }

      case "2" =>
        print("Enter username and sheet name: ")
        val input = scala.io.StdIn.readLine()
        val result = Try {
          val Array(userName, sheetName) = input.split(" ")
          (userName, sheetName)
        }

        result match {
          case Success((userName, sheetName)) =>
            createSheet(users, sheets, userName, sheetName) match {
              case Right(newSheets) =>
                println(s"Created a sheet named '$sheetName' for user '$userName'.")
                (users, newSheets)
              case Left(error) =>
                println(error)
                (users, sheets)
            }
          case Failure(_) =>
            println(s"Invalid input. Please enter the username and sheet name separated by a space.")
            (users, sheets)
        }

      case "3" =>
        print("Enter username and sheet name: ")
        val input = scala.io.StdIn.readLine()
        val result = Try {
          val Array(userName, sheetName) = input.split(" ")
          (userName, sheetName)
        }

        result match {
          case Success((userName, sheetName)) =>
            checkSheet(users, sheets, sheetName, userName, accessControl, sharingControl) match {
              case Right(data) => data.foreach(row => println(row.mkString(", ")))
              case Left(error) => println(error)
            }
          case Failure(_) =>
            println(s"Invalid input. Please enter the username and sheet name separated by a space.")
        }
        (users, sheets)

      case "4" =>
        print("Enter username and sheet name: ")
        val input1 = scala.io.StdIn.readLine()
        val userSheetResult = Try {
          val Array(userName, sheetName) = input1.split(" ")
          (userName, sheetName)
        }
        userSheetResult match {
          case Success((userName, sheetName)) =>
            checkSheet(users, sheets, sheetName, userName, accessControl, sharingControl) match {
              case Right(data) =>
                data.foreach(row => println(row.mkString(", ")))    
                print("Enter row, col, value: ")
                val input2 = scala.io.StdIn.readLine()
                val cellValueResult = Try {
                  val Array(row, col, value) = input2.split(" ")
                  (row.toInt, col.toInt, value)
                }
                cellValueResult match {
                  case Success((row, col, value)) =>
                    changeValue(users, sheets, userName, sheetName, row, col, value, accessControl, sharingControl) match {
                      case Right(newSheets) =>
                        checkSheet(users, newSheets, sheetName, userName, accessControl, sharingControl) match {
                          case Right(updatedData) => updatedData.foreach(row => println(row.mkString(", ")))
                          case Left(error) => println(error)
                        }
                        (users, newSheets)
                      case Left(error) =>
                        println(error)
                        (users, sheets)
                    }
                  case Failure(_) =>
                    println(s"Invalid input. Please enter the row and column as integers, followed by the value.")
                    (users, sheets)
                }
              case Left(error) =>
                println(error)
                (users, sheets)
            }
          case Failure(_) =>
            println(s"Invalid input. Please enter the username and sheet name separated by a space.")
            (users, sheets)
        }

      case "5" =>
        print("Enter username, sheet name and new access right (readonly/editable): ")
        val input = scala.io.StdIn.readLine()
        val result = Try {
          val Array(username, sheetName, right) = input.split(" ")
          (username, sheetName, right)
        }
        result match {
          case Success((username, sheetName, right)) =>
            changeAccessRight(users, sheets, username, sheetName, right, accessControl) match {
              case Right(newSheets) => 
                println(s"User '$username' changed the access right of sheet '$sheetName' to '$right'.")
                (users, newSheets)
              case Left(error) =>
                println(error)
                (users, sheets)
            }
          case Failure(_) =>
            println("Invalid input. Please enter the username, sheet name, and new access right separated by spaces.")
            (users, sheets)
        }

      case "6" =>
        print("Enter sheet name, owner name and collaborator name: ")
        val input = scala.io.StdIn.readLine()
        val result = Try {
          val Array(sheetName, ownerName, collaboratorName) = input.split(" ")
          (sheetName, ownerName, collaboratorName)
        }
        result match {
          case Success((sheetName, ownerName, collaboratorName)) =>
            shareSheet(users, sheets, ownerName, sheetName, collaboratorName, sharingControl) match {
              case Right(newSheets) => 
                println(s"User '$ownerName' shared sheet '$sheetName' with user '$collaboratorName'.")
                (users, newSheets)
              case Left(error) =>
                println(error)
                (users, sheets)
            }
          case Failure(_) =>
            println("Invalid input. Please enter the sheet name, owner name, and collaborator name separated by spaces.")
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

  // Entry point of the program
  def main(args: Array[String]): Unit = {
    var users: Users = Map()
    var sheets: Sheets = Map()
    val accessControl = EnableAccessControl
    val sharingControl = EnableSharingControl
    
    mainMenu(users, sheets, accessControl, sharingControl)
  }
}
