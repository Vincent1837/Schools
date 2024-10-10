import scala.collection.immutable.Map
import scala.util.{Try, Success, Failure}

object JDoodle {

  case class User(name: String)

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

  def createSheet(users: Users, sheets: Sheets, userName: String, sheetName: String): Either[String, Sheets] = {
    if (sheets.contains(sheetName)) {
      Left(s"Sheet '$sheetName' already exists.")
    } else {
      if (!users.contains(userName)) {
        Left(s"User '$userName' does not exist.")
      } else {
        val newSheet = Sheet(sheetName, Array.fill(3, 3)(0.0), "editable", userName, Set())
        Right(sheets + (sheetName -> newSheet))
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
            case Right(newSheets) => (users, newSheets)
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
        shareSheet(users, sheets, ownerName, sheetName, collaboratorName, sharingControl) match {
            case Right(newSheets) => 
                println(s"User '$ownerName' shared sheet '$sheetName' with user '$collaboratorName'.")
                (users, newSheets)
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

    // 測試創建用戶
    println("Creating user 'Alice'...")
    createUser(users, "Alice") match {
      case Right(newUsers) =>
        users = newUsers
        println(users)
      case Left(error) => println(error)
    }
    println()
    //測試創建第二個用戶
    println("Creating user 'Bob'...")
    createUser(users, "Bob") match {
      case Right(newUsers) =>
        users = newUsers
        println(users)
      case Left(error) => println(error)
    }
    println()
    // 測試創建工作表
    println("Creating sheet 'Sheet1' for user 'Alice'...")
    createSheet(users, sheets, "Alice", "Sheet1") match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試創建重複的用戶
    println("Creating user 'Alice' again...")
    createUser(users, "Alice") match {
      case Right(newUsers) =>
        users = newUsers
        println(users)
      case Left(error) => println(error)
    }
    println()
    // 測試創建重複的工作表
    println("Creating sheet 'Sheet1' again...")
    createSheet(users, sheets, "Bob", "Sheet1") match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試檢查工作表
    println("Checking sheet 'Sheet1' for user 'Alice'...")
    checkSheet(users, sheets, "Sheet1", "Alice", accessControl, sharingControl) match {
      case Right(data) => data.foreach(row => println(row.mkString(", ")))
      case Left(error) => println(error)
    }
    println()
    // 測試檢查不存在的工作表
    println("Checking sheet 'Sheet2' for user 'Alice'...")
    checkSheet(users, sheets, "Sheet2", "Alice", accessControl, sharingControl) match {
      case Right(data) => data.foreach(row => println(row.mkString(", ")))
      case Left(error) => println(error)
    }
    println()
    // 測試更改工作表中的值
    println("Changing value in 'Sheet1' for user 'Alice' at (0, 0) to '5.0 + 3.0'...")
    changeValue(users, sheets, "Alice", "Sheet1", 0, 0, "5.0 + 3.0", accessControl, sharingControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        checkSheet(users, sheets, "Sheet1", "Alice", accessControl, sharingControl) match {
          case Right(data) => data.foreach(row => println(row.mkString(", ")))
          case Left(error) => println(error)
        }
      case Left(error) => println(error)
    }
    println()
    // 測試更改工作表的訪問權限
    println("Changing access right of 'Alice's' 'Sheet1' to 'readonly'...")
    changeAccessRight(users, sheets, "Alice", "Sheet1", "readonly", accessControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試更改唯獨工作表中的值
    println("Changing value in 'Sheet1' for user 'Alice' at (0, 0) to '10.0 + 2.0'...")
    changeValue(users, sheets, "Alice", "Sheet1", 0, 0, "10.0 + 2.0", accessControl, sharingControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        checkSheet(users, sheets, "Sheet1", "Alice", accessControl, sharingControl) match {
          case Right(data) => data.foreach(row => println(row.mkString(", ")))
          case Left(error) => println(error)
        }
      case Left(error) => println(error)
    }
    println()
    // 測試分享工作表
    println("Sharing 'Sheet1' with 'Bob'...")
    createUser(users, "Bob") match {
      case Right(newUsers) =>
        users = newUsers
        println(users)
      case Left(error) => println(error)
    }
    shareSheet(users, sheets, "Alice", "Sheet1", "Bob", sharingControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試分享給不存在的用戶
    println("Sharing 'Sheet1' with 'Charlie'...")
    shareSheet(users, sheets, "Alice", "Sheet1", "Charlie", sharingControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試合作者檢查共享的工作表
    println("Checking sheet 'Sheet1' for user 'Bob'...")
    checkSheet(users, sheets, "Sheet1", "Bob", accessControl, sharingControl) match {
      case Right(data) => data.foreach(row => println(row.mkString(", ")))
      case Left(error) => println(error)
    }
    println()
    // 測試更改工作表的訪問權限
    println("Changing access right of 'Alice's' 'Sheet1' to 'editable'...")
    changeAccessRight(users, sheets, "Alice", "Sheet1", "editable", accessControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試合作者更改工作表的訪問權限
    println("Changing access right of 'Sheet1' to 'readonly' by 'Bob'...")
    changeAccessRight(users, sheets, "Bob", "Sheet1", "readonly", accessControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        println(sheets)
      case Left(error) => println(error)
    }
    println()
    // 測試合作者更改工作表中的值
    println("Changing value in 'Sheet1' for user 'Bob' at (0, 0) to '10.0 + 3.0'...")
    changeValue(users, sheets, "Bob", "Sheet1", 0, 0, "10 + 3", accessControl, sharingControl) match {
      case Right(newSheets) =>
        sheets = newSheets
        checkSheet(users, sheets, "Sheet1", "Bob", accessControl, sharingControl) match {
          case Right(data) => data.foreach(row => println(row.mkString(", ")))
          case Left(error) => println(error)
        }
      case Left(error) => println(error)
    }
    println()
    // 測試合作者更改結果
    println("Checking sheet 'Sheet1' for user 'Alice'...")
    checkSheet(users, sheets, "Sheet1", "Alice", accessControl, sharingControl) match {
      case Right(data) => data.foreach(row => println(row.mkString(", ")))
      case Left(error) => println(error)
    }
    
    mainMenu(users, sheets, accessControl, sharingControl)
  }
}