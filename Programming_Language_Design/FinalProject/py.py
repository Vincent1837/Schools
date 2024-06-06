class User:
    def __init__(self, name):
        self.name = name
        self.sheets = {}

    def create_sheet(self, sheet_name):
        if sheet_name in self.sheets:
            print(f"Sheet {sheet_name} already exists.")
        else:
            self.sheets[sheet_name] = Sheet(sheet_name)
            print(f"Create a sheet named \"{sheet_name}\" for \"{self.name}\".")

    def get_sheet(self, sheet_name):
        return self.sheets.get(sheet_name)

class Sheet:
    def __init__(self, name):
        self.name = name
        self.data = [[0 for _ in range(3)] for _ in range(3)]

    def print_sheet(self):
        for row in self.data:
            print(", ".join(map(str, row)))
        print()

    def change_value(self, row, col, value):
        try:
            if '+' in value or '-' in value or '*' in value or '/' in value:
                self.data[row][col] = eval(value)
            else:
                self.data[row][col] = float(value)
        except Exception as e:
            print("Invalid value.")
        self.print_sheet()

class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, name):
        if name in self.users:
            print(f"User {name} already exists.")
        else:
            self.users[name] = User(name)
            print(f"Create a user named \"{name}\".")

    def get_user(self, name):
        return self.users.get(name)

class SheetManager:
    def __init__(self, access=True, collaboration=True):
        self.access_rights = {}
        self.shared_sheets = {}
        self.access = access
        self.collaboration = collaboration

    def set_access_rights(self, sheet_name, rights):
        self.access_rights[sheet_name] = rights
        print(f"Sheet access rights set to {rights}")

    def get_access_rights(self, sheet_name):
        return self.access_rights.get(sheet_name, "Editable")

    def share_sheet(self, user, sheet_name, target_user):
        if sheet_name not in self.shared_sheets:
            self.shared_sheets[sheet_name] = []
        self.shared_sheets[sheet_name].append(target_user)
        print(f"Share \"{user.name}\"'s \"{sheet_name}\" with \"{target_user.name}\".")

    def is_shared_with(self, sheet_name, user):
        return user in self.shared_sheets.get(sheet_name, [])

class Facade:
    def __init__(self):
        self.user_manager = UserManager()
        self.sheet_manager = SheetManager()

    def create_user(self, name):
        self.user_manager.create_user(name)

    def create_sheet(self, user_name, sheet_name):
        user = self.user_manager.get_user(user_name)
        if user:
            user.create_sheet(sheet_name)
        else:
            print(f"User {user_name} not found.")

    def check_sheet(self, user_name, sheet_name):
        user = self.user_manager.get_user(user_name)
        if user:
            sheet = user.get_sheet(sheet_name)
            if sheet:
                sheet.print_sheet()
            else:
                print(f"Sheet {sheet_name} not found.")
        else:
            print(f"User {user_name} not found.")

    def change_value(self, user_name, sheet_name, row, col, value):
        user = self.user_manager.get_user(user_name)
        if user:
            sheet = user.get_sheet(sheet_name)
            if sheet:
                rights = self.sheet_manager.get_access_rights(sheet_name)
                if rights == "ReadOnly":
                    print("This sheet is not accessible.")
                else:
                    sheet.change_value(row, col, value)
            else:
                print(f"Sheet {sheet_name} not found.")
        else:
            print(f"User {user_name} not found.")

    def change_access_rights(self, user_name, sheet_name, rights):
        user = self.user_manager.get_user(user_name)
        if user:
            sheet = user.get_sheet(sheet_name)
            if sheet:
                self.sheet_manager.set_access_rights(sheet_name, rights)
            else:
                print(f"Sheet {sheet_name} not found.")
        else:
            print(f"User {user_name} not found.")

    def collaborate(self, user_name, sheet_name, target_user_name):
        user = self.user_manager.get_user(user_name)
        target_user = self.user_manager.get_user(target_user_name)
        if user and target_user:
            sheet = user.get_sheet(sheet_name)
            if sheet:
                self.sheet_manager.share_sheet(user, sheet_name, target_user)
            else:                  
                print(f"Sheet {sheet_name} not found.")
        else:
            print(f"User {user_name} or {target_user_name} not found.")

def main():
    facade = Facade()                                         

    while True:
        print("---------------Menu---------------")
        print("1. Create a user")
        print("2. Create a sheet")
        print("3. Check a sheet")
        print("4. Change a value in a sheet")
        print("5. Change a sheet's access right")
        print("6. Collaborate with an other user")
        print("----------------------------------")
        choice = input("> ")

        if choice == "1":
            name = input("> ")
            facade.create_user(name)

        elif choice == "2":
            user_name, sheet_name = input("> ").split()
            facade.create_sheet(user_name, sheet_name)

        elif choice == "3":
            user_name, sheet_name = input("> ").split()
            facade.check_sheet(user_name, sheet_name)

        elif choice == "4":
            user_name, sheet_name = input("> ").split()
            facade.check_sheet(user_name, sheet_name)
            row, col, value = input("> ").split()
            facade.change_value(user_name, sheet_name, int(row), int(col), value)

        elif choice == "5":
            user_name, sheet_name, rights = input("> ").split()
            facade.change_access_rights(user_name, sheet_name, rights)

        elif choice == "6":
            user_name, sheet_name, target_user_name = input("> ").split()
            facade.collaborate(user_name, sheet_name, target_user_name)

if __name__ == "__main__":
    main()