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