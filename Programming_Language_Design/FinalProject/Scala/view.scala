class ConsoleView(userController: UserController, sheetController: SheetController) {
  def mainMenu(): Unit = {
    println("---------------Menu---------------")
    println("1. Create a user")
    println("2. Create a sheet")
    println("3. Check a sheet")
    println("4. Change a value in a sheet")
    println("5. Change a sheet's access right.")
    println("6. Collaborate with another user")
    println("----------------------------------")
    println("> ")

    scala.io.StdIn.readInt() match {
      case 1 => createUser()
      case 2 => createSheet()
      case 3 => checkSheet()
      case 4 => changeCellValue()
      case 5 => changeSheetAccessRight()
      case 6 => collaborate()
      case _ => println("Invalid option")
    }
  }

  def createUser(): Unit = {
    println("Enter username:")
    val username = scala.io.StdIn.readLine()
    userController.createUser(username)
  }

  def createSheet(): Unit = {
    println("Enter owner name and sheet name:")
    val input = scala.io.StdIn.readLine().split(" ")
    val owner = userController.findUser(input(0))
    owner match {
      case Some(user) => sheetController.createSheet(input(1), user)
      case None => println("User not found")
    }
  }

  def checkSheet(): Unit = {
    println("Enter owner name and sheet name:")
    val input = scala.io.StdIn.readLine().split(" ")
    val owner = userController.findUser(input(0))
    owner match {
      case Some(user) => sheetController.findSheet(input(1), user) match {
        case Some(sheet) => sheet.printSheet()
        case None => println("Sheet not found")
      }
      case None => println("User not found")
    }
  }

  def changeCellValue(): Unit = {
    println("Enter owner name, sheet name, row, col, and new content:")
    val input = scala.io.StdIn.readLine().split(" ")
    val owner = userController.findUser(input(0))
    owner match {
      case Some(user) => sheetController.findSheet(input(1), user) match {
        case Some(sheet) =>
          val row = input(2).toInt
          val col = input(3).toInt
          sheet.updateCell(row, col, input(4))
        case None => println("Sheet not found")
      }
      case None => println("User not found")
    }
  }

  def changeSheetAccessRight(): Unit = {
    println("Enter owner name, sheet name, and new access right:")
    val input = scala.io.StdIn.readLine().split(" ")
    val owner = userController.findUser(input(0))
    owner match {
      case Some(user) => sheetController.findSheet(input(1), user) match {
        case Some(sheet) => sheet.accessRights += (user -> input(2))
        case None => println("Sheet not found")
      }
      case None => println("User not found")
    }
  }

  def collaborate(): Unit = {
    println("Enter owner name, sheet name, and collaborator name:")
    val input = scala.io.StdIn.readLine().split(" ")
    val owner = userController.findUser(input(0))
    val collaborator = userController.findUser(input(2))
    (owner, collaborator) match {
      case (Some(user), Some(collab)) => sheetController.findSheet(input(1), user) match {
        case Some(sheet) => sheet.shareWith(collab, "read")
        case None => println("Sheet not found")
      }
      case _ => println("User or collaborator not found")
    }
  }
}