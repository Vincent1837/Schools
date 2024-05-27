case class User(name: String)
case class Cell(content: String)
case class Sheet(name: String, owner: User, cells: Array[Array[Cell]], var accessRights: Map[User, String]) {
  def printSheet(): Unit = cells.foreach(row => println(row.map(_.content).mkString(", ")))
  def updateCell(row: Int, col: Int, newContent: String): Unit = cells(row)(col) = Cell(newContent)
  def shareWith(user: User, accessRight: String): Unit = accessRights += (user -> accessRight)
}