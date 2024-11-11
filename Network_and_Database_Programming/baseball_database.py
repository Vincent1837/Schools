import wx
import os
import pymongo
import wx.lib.filebrowsebutton as filebrowse
import wx.lib.scrolledpanel as scrolled

# MongoDB 連線設置
client = pymongo.MongoClient("mongodb+srv://yuanchan1837:yuanchan1837@cluster0.dc6xs.mongodb.net/")
db = client['baseball']
team_collection = db['teams']
player_collection = db['players']
match_collection = db['matches']



class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(650, 500))
        panel = wx.Panel(self)

        notebook = wx.Notebook(panel)
        
        # 新增球隊資料
        self.team_panel = scrolled.ScrolledPanel(notebook)
        self.team_panel.SetScrollRate(5, 5)
        self.create_team_panel(self.team_panel)
        notebook.AddPage(self.team_panel, "Add new Team")
        
        # 新增球員資料
        self.player_panel = scrolled.ScrolledPanel(notebook)
        self.player_panel.SetScrollRate(5, 5)
        self.create_player_panel(self.player_panel)
        notebook.AddPage(self.player_panel, "Add new Player")

        self.displaying_panel = scrolled.ScrolledPanel(notebook)
        self.display_panel(self.displaying_panel)
        notebook.AddPage(self.displaying_panel, "Display")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

    def create_team_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.tname_textCtrl = wx.TextCtrl(panel)
        self.tcity_textCtrl = wx.TextCtrl(panel)
        self.tfield_textCtrl = wx.TextCtrl(panel)
        self.tlogo_btn = filebrowse.FileBrowseButton(panel, labelText="Team LOGO", fileMask="*.png;*.jpg;*.jpeg")
        create_team_button = wx.Button(panel, label="Create Team")
        create_team_button.Bind(wx.EVT_BUTTON, self.on_create_team)
        
        vbox.Add(wx.StaticText(panel, label="Team Name"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.tname_textCtrl, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="City"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.tcity_textCtrl, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="Home Field"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.tfield_textCtrl, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.tlogo_btn, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(create_team_button, flag=wx.EXPAND | wx.ALL, border=5)
        
        panel.SetSizer(vbox)
        
    def on_create_team(self, event):
        # Get values from form fields
        tname = self.tname_textCtrl.GetValue()
        tcity = self.tcity_textCtrl.GetValue()
        tfield = self.tfield_textCtrl.GetValue()
        tlogo_path = self.tlogo_btn.GetValue()
        print(tlogo_path)
        
        if not tname or not tcity or not tfield or not tlogo_path:
            wx.MessageBox("Please fill in all fields.", "Error", wx.ICON_ERROR)
            return

        # Show confirmation dialog
        message = f"Creating:\n\nTeam Name: {tname}\nCity: {tcity}\nField: {tfield}"
        dialog = ConfirmationDialog(self, "Confirm Team Creation", message, tlogo_path)
        dialog.ShowModal()
        
        if dialog.result:
            # Confirm and add to database
            new_team = {
                'name': tname,
                'city': tcity,
                'field': tfield,
                'logo': tlogo_path
            }
            team_collection.insert_one(new_team)
            wx.MessageBox("Team created successfully!", "Success", wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Team creation canceled.", "Canceled", wx.ICON_WARNING)
        dialog.Destroy()
        
    # Create Player Data Panel
    def create_player_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.fname_textCtrl = wx.TextCtrl(panel)
        self.lname_textCtrl = wx.TextCtrl(panel)
        self.team_textCtrl = wx.TextCtrl(panel)
        self.position_textCtrl = wx.TextCtrl(panel)
        self.number_textCtrl = wx.TextCtrl(panel)
        self.height_textCtrl = wx.TextCtrl(panel)
        self.weight_textCtrl = wx.TextCtrl(panel)
        self.bats_throws_textCtrl = wx.TextCtrl(panel)
        self.age_textCtrl = wx.TextCtrl(panel)
        self.player_photo_btn = filebrowse.FileBrowseButton(panel, labelText="Player Photo", fileMask="*.png;*.jpg;*.jpeg")

        
        create_player_button = wx.Button(panel, label="Create Player")
        create_player_button.Bind(wx.EVT_BUTTON, self.on_create_player)
        
        fields = [
            ("First Name", self.fname_textCtrl),
            ("Last Name", self.lname_textCtrl),
            ("Team", self.team_textCtrl),
            ("Position", self.position_textCtrl),
            ("Number", self.number_textCtrl),
            ("Height", self.height_textCtrl),
            ("Weight", self.weight_textCtrl),
            ("Bats/Throws", self.bats_throws_textCtrl),
            ("Age", self.age_textCtrl)
        ]
        
        for label, ctrl in fields:
            vbox.Add(wx.StaticText(panel, label=label), flag=wx.EXPAND | wx.ALL, border=5)
            vbox.Add(ctrl, flag=wx.EXPAND | wx.ALL, border=5)
            
        vbox.Add(self.player_photo_btn, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(create_player_button, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)
        
    def on_create_player(self, event):
        # Get values from form fields
        fname = self.fname_textCtrl.GetValue()
        lname = self.lname_textCtrl.GetValue()
        team = self.team_textCtrl.GetValue()
        position = self.position_textCtrl.GetValue()
        number = self.number_textCtrl.GetValue()
        height = self.height_textCtrl.GetValue()
        weight = self.weight_textCtrl.GetValue()
        bats_throws = self.bats_throws_textCtrl.GetValue()
        age = self.age_textCtrl.GetValue()
        photo_path = self.player_photo_btn.GetValue()
        
        # Check if all values have been entered
        if not all([fname, lname, team, position, number, height, weight, bats_throws, age, photo_path]):
            wx.MessageBox("Please fill in all fields.", "Error", wx.ICON_ERROR)
            return

        # Show confirmation dialog
        message = f"Creating:\n\nPlayer: {fname} {lname}\nTeam: {team}\nPosition: {position}\nNumber: {number}\n" \
                  f"Height: {height}\nWeight: {weight}\nBats/Throws: {bats_throws}\nAge: {age}"
        dialog = ConfirmationDialog(self, "Confirm Player Creation", message, photo_path)
        dialog.ShowModal()
        
        if dialog.result:
            # Team not found
            if list(team_collection.find({'name': team})).__len__() == 0:
                wx.MessageBox("Team does not exist.", "Error", wx.ICON_ERROR)
            
            else:   
                # Confirm and add to database
                new_player = {
                    'first_name': fname,
                    'last_name': lname,
                    'team': team,
                    'position': position,
                    'number': number,
                    'height': height,
                    'weight': weight,
                    'bats_throws': bats_throws,
                    'age': age,
                    'photo_path': photo_path
                }
                player_collection.insert_one(new_player)
                wx.MessageBox("Player created successfully!", "Success", wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Player creation canceled.", "Canceled", wx.ICON_WARNING)
        dialog.Destroy()

    def display_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Refresh Button
        refresh_button = wx.Button(panel, label="Refresh")
        refresh_button.Bind(wx.EVT_BUTTON, self.display_panel)
        vbox.Add(refresh_button, flag=wx.EXPAND | wx.ALL, border=10)
        
        # Fetch all teams from the database
        teams = team_collection.find()
        for team in teams:
            team_name = team['name']
            team_city = team['city']
            team_logo = team['logo']
            
            logo_bitmap = wx.Bitmap(loadImg(team_logo, 100, 100))
            team_button = wx.Button(panel, label=f"{team_city} {team_name}", size=(650, 100))
            team_button.SetBitmap(logo_bitmap)
            
            team_button.Bind(wx.EVT_BUTTON, lambda evt, name=team_name: self.on_show_players(evt, name))
            vbox.Add(team_button, flag=wx.EXPAND | wx.ALL, border=5)
        
        # Scrollable panel for team buttons
        """ self.team_sizer = wx.BoxSizer(wx.VERTICAL)
        scroll_panel = wx.ScrolledWindow(panel, style=wx.VSCROLL)
        scroll_panel.SetSizer(self.team_sizer)
        scroll_panel.SetScrollRate(0, 20)
        
        vbox.Add(scroll_panel, proportion=1, flag=wx.EXPAND) """
        panel.SetSizer(vbox)
        
        # Initial load of teams
        #self.load_teams(panel)
        
    def load_teams(self, panel):
        # Clear current team buttons
        for child in self.team_sizer.GetChildren():
            child.GetWindow().Destroy()

        # Fetch all teams from the database
        teams = team_collection.find()

        for team in teams:
            team_name = team['name']
            team_city = team['city']
            team_logo = team.get('logo', '')

            # Add team button with or without logo
            if os.path.exists(team_logo):
                # Use wx.BitmapButton with 'panel' as the parent
                logo_bitmap = wx.Bitmap(team_logo, wx.BITMAP_TYPE_ANY)
                team_button = wx.BitmapButton(panel, bitmap=logo_bitmap, size=(80, 80))
                team_button.SetToolTip(f"{team_city} {team_name}")
            else:
                # Use wx.Button with 'panel' as the parent
                team_button = wx.Button(self.panel, label=f"{team_city} {team_name}", size=(200, 30))

            # Bind button event to display players dialog
            team_button.Bind(wx.EVT_BUTTON, lambda evt, name=team_name: self.on_show_players(evt, name))
            
            # Add each team button to team_sizer
            self.team_sizer.Add(team_button, flag=wx.EXPAND | wx.ALL, border=5)

        # Refresh layout after loading buttons
        self.vbox.Layout()

    
    def on_show_players(self, event, team_name):
        dialog = PlayerDialog(self, "Team Players", team_name)
        dialog.ShowModal()
        dialog.Destroy()
        
        
    
    
class ConfirmationDialog(wx.Dialog):
    def __init__(self, parent, title, message, img_path=None):
        super(ConfirmationDialog, self).__init__(parent, title=title, size=(400, 400))
        panel = wx.Panel(self)
        
        if img_path:
            self.image = loadImg(img_path, )
            self.logo_bitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap(self.image))

        vbox = wx.BoxSizer(wx.VERTICAL)
        #vbox.Add(self.logo_bitmap, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(wx.StaticText(panel, label=message), flag=wx.EXPAND | wx.ALL, border=10)
        
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.confirm_button = wx.Button(panel, label="Confirm")
        self.back_button = wx.Button(panel, label="Back")
        
        button_sizer.Add(self.back_button, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(self.confirm_button, flag=wx.EXPAND | wx.ALL, border=5)
        
        vbox.Add(button_sizer, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.logo_bitmap, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(vbox, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(hbox)
        
        self.Bind(wx.EVT_BUTTON, self.on_confirm, self.confirm_button)
        self.Bind(wx.EVT_BUTTON, self.on_back, self.back_button)
        
        self.result = None
    
    def on_confirm(self, event):
        self.result = True
        self.Close()
    
    def on_back(self, event):
        self.result = False
        self.Close()
        
class PlayerDialog(wx.Dialog):
    def __init__(self, parent, title, team_name):
        super(PlayerDialog, self).__init__(parent, title=title, size=(400, 500))
        
        # Retrieve players for the selected team
        players = player_collection.find({'team': team_name})
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        for player in players:
            # Display player information with photo
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            
            # Load player photo
            photo_path = player['photo_path']
            if os.path.exists(photo_path):
                player_photo = wx.StaticBitmap(panel, bitmap=wx.Bitmap(loadImg(photo_path, 100, 100)))
            else:
                player_photo = wx.StaticText(panel, label="No Image")

            # Player info
            player_info = (
                f"Name: {player['first_name']} {player['last_name']}\n"
                f"Position: {player['position']}\n"
                f"Number: {player['number']}\n"
                f"Height: {player['height']}\n"
                f"Weight: {player['weight']}\n"
                f"Bats/Throws: {player['bats_throws']}\n"
                f"Age: {player['age']}"
            )
            player_text = wx.StaticText(panel, label=player_info)

            hbox.Add(player_photo, flag=wx.ALL, border=5)
            hbox.Add(player_text, flag=wx.ALL, border=5)
            vbox.Add(hbox, flag=wx.EXPAND | wx.ALL, border=10)
        
        panel.SetSizer(vbox)
        

def loadImg(img_path, h=170, w=170):
        image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        height = image.GetHeight()
        width = image.GetWidth()
        image.Resize(wx.Size(max(height, width), max(height, width)), wx.Point(0, 0))
        image.Rescale(h, w)
        return image

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, "Baseball Database")
    frame.Show()
    frame.Center()
    app.MainLoop()
