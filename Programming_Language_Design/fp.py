class User:
    def __init__(self, name):
        self.name = name
        self.owned_sheets = []
        self.shared_sheets = []

    def add_owned_sheet(self, sheet):
        self.owned_sheets.append(sheet)

    def add_shared_sheet(self, sheet):
        self.shared_sheets.append(sheet)

class Sheet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.data = [[0]*3 for _ in range(3)]

    def change_content(self, row, col, value):
        self.data[row][col] = eval(value)

    def print_sheet(self):
        for row in self.data:
            print(", ".join(map(str, row)))
        print()

class SheetDecorator(Sheet):
    def __init__(self, sheet):
        self._sheet = sheet

    def change_content(self, row, col, value):
        self._sheet.change_content(row, col, value)

    def print_sheet(self):
        self._sheet.print_sheet()

class AccessControlDecorator(SheetDecorator):
    def __init__(self, sheet):
        super().__init__(sheet)
        self.access_rights = {self._sheet.owner.name: 'Editable'}

    def change_content(self, row, col, value):
        if self.access_rights.get(self._sheet.owner.name) == 'Editable':
            super().change_content(row, col, value)
        else:
            raise PermissionError("This sheet is not accessible.")

class ShareDecorator(SheetDecorator):
    def __init__(self, sheet):
        super().__init__(sheet)
        self.shared_with = []

    def share_with(self, user):
        self.shared_with.append(user)
        print(f'Sheet shared with {user.name}')

class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)
            print(f'Create a user named "{name}".')
        else:
            print(f'User "{name}" already exists.')

    def get_user(self, name):
        return self.users.get(name)

class SheetManager:
    def __init__(self, user_manager, access_control=True, share=True):
        self.user_manager = user_manager
        self.sheets = {}
        self.access_control = access_control
        self.share = share

    def create_sheet(self, user_name, sheet_name):
        user = self.user_manager.get_user(user_name)
        if user:
            sheet = Sheet(sheet_name, user)
            if self.access_control:
                sheet = AccessControlDecorator(sheet)
            if self.share:
                sheet = ShareDecorator(sheet)
            self.sheets[(user_name, sheet_name)] = sheet
            user.add_owned_sheet(sheet)
            print(f'Create a sheet named "{sheet_name}" for "{user_name}".')
        else:
            print(f'User "{user_name}" does not exist.')

    def check_sheet(self, user_name, sheet_name):
        sheet = self.get_sheet(user_name, sheet_name)
        if sheet:
            sheet.print_sheet()

    def change_value(self, user_name, sheet_name, row, col, value):
        sheet = self.get_sheet(user_name, sheet_name)
        if sheet:
            try:
                sheet.change_content(row, col, value)
                print(f'Change value at ({row}, {col}) to {value}.')
            except PermissionError as e:
                print(e)

    def collaborate(self, owner_name, sheet_name, collaborator_name):
        sheet = self.get_sheet(owner_name, sheet_name)
        collaborator = self.user_manager.get_user(collaborator_name)
        if sheet and collaborator:
            sheet.share_with(collaborator)
            collaborator.add_shared_sheet(sheet)
        else:
            print(f'Sheet "{sheet_name}" is not sharable or user "{collaborator_name}" does not exist.')

    def change_access(self, user_name, sheet_name, access):
        sheet = self.get_sheet(user_name, sheet_name)
        if sheet and isinstance(sheet, AccessControlDecorator):
            sheet.access_rights[user_name] = access
            print(f'Change access for "{user_name}" to "{access}".')
        else:
            print(f'Sheet "{sheet_name}" does not support access control.')

    def get_sheet(self, user_name, sheet_name):
        return self.sheets.get((user_name, sheet_name))

def main():
    user_manager = UserManager()
    sheet_manager = SheetManager(user_manager)

    user_manager.create_user('k')
    sheet_manager.create_sheet('k', 'a')
    sheet_manager.check_sheet('k', 'a')
    sheet_manager.change_value('k', 'a', 0, 0, '1')
    sheet_manager.change_access('k', 'a', 'ReadOnly')
    sheet_manager.change_value('k', 'a', 0, 0, '2')
    user_manager.create_user('l')
    sheet_manager.collaborate('k', 'a', 'l')

if __name__ == "__main__":
    main()