object MainApp {
  def main(args: Array[String]): Unit = {
    val userController = new UserController()
    val sheetController = new SheetController()
    val view = new ConsoleView(userController, sheetController)

    while (true) {
      view.mainMenu()
    }
  }
}