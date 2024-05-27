class UserController {
  private var users: List[User] = List()

  def createUser(name: String): User = {
    val user = User(name)
    users = user :: users
    user
  }

  def findUser(name: String): Option[User] = users.find(_.name == name)
}

class SheetController {
  private var sheets: List[Sheet] = List()

  def createSheet(name: String, owner: User): Sheet = {
    val sheet = Sheet(name, owner, Array.fill(3, 3)(Cell("0")), Map(owner -> "editable"))
    sheets = sheet :: sheets
    sheet
  }

  def findSheet(name: String, owner: User): Option[Sheet] = sheets.find(s => s.name == name && s.owner == owner)
}