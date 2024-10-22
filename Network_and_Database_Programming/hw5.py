import wx
import pymongo
import wx.lib.filebrowsebutton as filebrowse

# MongoDB 連線設置
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['school']
student_collection = db['students']
course_collection = db['courses']
enrollment_collection = db['enrollments']

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(650, 500))
        panel = wx.Panel(self)

        # 分成七個功能區塊
        notebook = wx.Notebook(panel)
        
        # 新增學生資料
        self.student_panel = wx.Panel(notebook)
        self.create_student_panel(self.student_panel)
        notebook.AddPage(self.student_panel, "新增學生資料")

        # 新增課程資料
        self.course_panel = wx.Panel(notebook)
        self.create_course_panel(self.course_panel)
        notebook.AddPage(self.course_panel, "新增課程資料")

        # 新增選課資料
        self.enrollment_panel = wx.Panel(notebook)
        self.create_enrollment_panel(self.enrollment_panel)
        notebook.AddPage(self.enrollment_panel, "新增選課資料")
        
        # 輸入期中與期末成績
        self.midterm_panel = wx.Panel(notebook)
        self.enter_midterm_score(self.midterm_panel)
        notebook.AddPage(self.midterm_panel, "輸入期中期末成績")

        # 查詢總成績
        self.query_panel = wx.Panel(notebook)
        self.create_query_panel(self.query_panel)
        notebook.AddPage(self.query_panel, "查詢總成績")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

    # 新增學生資料區塊
    def create_student_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.sid_txt = wx.TextCtrl(panel) 
        self.fname_txt = wx.TextCtrl(panel)  
        self.lname_txt = wx.TextCtrl(panel)  
        self.grade_rbox = wx.RadioBox(panel, label="年級", choices=['1', '2', '3', '4', '5', '6'])
        self.sex_rbox = wx.RadioBox(panel, label="性別", choices=['男', '女'])
        self.email_txt = wx.TextCtrl(panel)
        self.photo_btn = filebrowse.FileBrowseButton(panel, labelText="學生照片", fileMask="*.png;*.jpg;*.jpeg")
        
        submit_btn1 = wx.Button(panel, label="新增學生資料")
        submit_btn1.Bind(wx.EVT_BUTTON, self.on_add_student)
        
        vbox.Add(wx.StaticText(panel, label="學號"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.sid_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="名字"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.fname_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="姓氏"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.lname_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.grade_rbox, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.sex_rbox, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="E-mail"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.email_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.photo_btn, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(submit_btn1, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)

    def on_add_student(self, event):
        sid = self.sid_txt.GetValue()
        fname = self.fname_txt.GetValue()
        lname = self.lname_txt.GetValue()
        grade = self.grade_rbox.GetStringSelection()
        sex = self.sex_rbox.GetStringSelection()
        email = self.email_txt.GetValue()
        photo_path = self.photo_btn.GetValue()

        # 儲存到 MongoDB
        student_data = {
            "sid": sid,
            "fname": fname,
            "lname": lname,
            "grade": grade,
            "sex": sex,
            "email": email,
            "photo": photo_path
        }
        student_collection.insert_one(student_data)
        
        wx.MessageBox(f"學生 {fname} {lname} 已新增", "訊息", wx.OK | wx.ICON_INFORMATION)

    # 新增課程資料區塊
    def create_course_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.cid_txt = wx.TextCtrl(panel)
        self.cname_txt = wx.TextCtrl(panel)
        submit_btn2 = wx.Button(panel, label="新增課程資料")
        submit_btn2.Bind(wx.EVT_BUTTON, self.on_add_course)

        vbox.Add(wx.StaticText(panel, label="課程號碼"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cid_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="課名"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cname_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(submit_btn2, flag=wx.EXPAND | wx.ALL, border=5)    
        panel.SetSizer(vbox)

    def on_add_course(self, event):
        cid = self.cid_txt.GetValue()
        cname = self.cname_txt.GetValue()

        # 儲存到 MongoDB
        course_data = {
            "cid": cid,
            "cname": cname
        }
        course_collection.insert_one(course_data)
        
        wx.MessageBox(f"課程 {cname} 已新增", "訊息", wx.OK | wx.ICON_INFORMATION)

    def create_enrollment_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sid_enroll_txt = wx.TextCtrl(panel)
        self.cid_enroll_txt = wx.TextCtrl(panel)
        submit_btn3 = wx.Button(panel, label="新增選課資料")
        submit_btn3.Bind(wx.EVT_BUTTON, self.on_add_enrollment)

        vbox.Add(wx.StaticText(panel, label="學號"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.sid_enroll_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="課程號碼"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cid_enroll_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(submit_btn3, flag=wx.EXPAND | wx.ALL, border=5)
        
        panel.SetSizer(vbox)

    def on_add_enrollment(self, event):
        sid = self.sid_enroll_txt.GetValue()
        cid = self.cid_enroll_txt.GetValue()
        enrollment_data = {
            "sid": sid,
            "cid": cid,
            "midScore": 0,
            "finalScore": 0
        }
        enrollment_collection.insert_one(enrollment_data)
        wx.MessageBox(f"選課資料已新增", "訊息", wx.OK | wx.ICON_INFORMATION)

    # 新增期中與期末成績
    def enter_midterm_score(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sid_midterm_txt = wx.TextCtrl(panel)
        self.cid_midterm_txt = wx.TextCtrl(panel)
        self.midterm_score_txt = wx.TextCtrl(panel)
        self.final_score_txt = wx.TextCtrl(panel)
        submit_btn4 = wx.Button(panel, label="新增期中與期末成績")
        submit_btn4.Bind(wx.EVT_BUTTON, self.on_add_mid)

        vbox.Add(wx.StaticText(panel, label="學號"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.sid_midterm_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="課程號碼"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cid_midterm_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="期中成績"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.midterm_score_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="期末成績"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.final_score_txt, flag=wx.EXPAND | wx.ALL, border=5)
        
        vbox.Add(submit_btn4, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)

    def on_add_mid(self, event):
        sid = self.sid_midterm_txt.GetValue()
        cid = self.cid_midterm_txt.GetValue()
        mid = float(self.midterm_score_txt.GetValue())
        final = float(self.final_score_txt.GetValue())

        # 儲存到 MongoDB
        enrollment_data = {
            "sid": sid,
            "cid": cid,
            "midScore": mid,
            "finalScore": final
        }
        enrollment_collection.update_one(
            {
                "$and": [
                    {"sid": sid},  # Condition 1
                    {"cid": cid}   # Condition 2
                ]
            },
            {
                "$set": {"midScore": mid, "finalScore": final}  # Update operation
            }
        )

        wx.MessageBox(f"期中與期末成績已新增", "訊息", wx.OK | wx.ICON_INFORMATION)


    # 查詢總成績區塊
    def create_query_panel(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.cid_query_txt = wx.TextCtrl(panel)
        query_btn = wx.Button(panel, label="查詢總成績")
        query_btn.Bind(wx.EVT_BUTTON, self.on_query_scores)

        vbox.Add(wx.StaticText(panel, label="課程號碼"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cid_query_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(query_btn, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)

    def on_query_scores(self, event):
        cid = self.cid_query_txt.GetValue()
        enrollments = enrollment_collection.find({"cid": cid})

        student_data = []
        for enrollment in enrollments:
            sid = enrollment["sid"]
            student = student_collection.find_one({"sid": sid})
            mid = enrollment["midScore"]
            final = enrollment["finalScore"]
            total = 0.4 * mid + 0.6 * final
            
            student_info = {
                'photo': student['photo'],
                'sid': student['sid'],
                'fname': student['fname'],
                'lname': student['lname'],
                'mid': mid,
                'final': final,
                'total': total,
                'email': student['email']
            }
            student_data.append(student_info)

        # Show the student data in the custom dialog
        dialog = StudentInfoDialog(self, student_data)
        dialog.ShowModal()

class StudentInfoDialog(wx.Dialog):
    def __init__(self, parent, student_data):
        super(StudentInfoDialog, self).__init__(parent, title="Student Information", size=(600, 400))

        # Create a scrolled window inside the dialog
        scrolled_panel = wx.ScrolledWindow(self, size=(580, 350), style=wx.VSCROLL)
        scrolled_panel.SetScrollRate(5, 5)  # Set scroll rate
        vbox = wx.BoxSizer(wx.VERTICAL)

        for student in student_data:
            # Load and display student photo
            image = wx.Image(student['photo'], wx.BITMAP_TYPE_ANY).Scale(100, 100)
            bitmap = wx.StaticBitmap(scrolled_panel, -1, wx.Bitmap(image))

            # Student details (name, scores, email)
            info = wx.StaticText(scrolled_panel, label=f"ID: {student['sid']}\n"
                                                       f"Name: {student['fname']} {student['lname']}\n"
                                                       f"Midterm Score: {student['mid']}\n"
                                                       f"Final Score: {student['final']}\n"
                                                       f"Total: {student['total']:.2f}\n"
                                                       f"Email: {student['email']}\n")

            # Layout for each student: horizontal box sizer
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            hbox.Add(bitmap, 0, wx.ALL, 5)
            hbox.Add(info, 0, wx.ALL, 5)

            # Add each student's details to the vertical sizer
            vbox.Add(hbox, 0, wx.ALL | wx.EXPAND, 5)

        # Set the sizer for the scrolled panel and adjust scrollbars
        scrolled_panel.SetSizer(vbox)
        scrolled_panel.Layout()

        # Add an OK button to close the dialog
        ok_button = wx.Button(self, label="OK")
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        # Main vertical layout for dialog
        dialog_vbox = wx.BoxSizer(wx.VERTICAL)
        dialog_vbox.Add(scrolled_panel, 1, wx.EXPAND | wx.ALL, 10)
        dialog_vbox.Add(ok_button, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(dialog_vbox)
        self.Centre()

    def on_ok(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, "學生管理系統")
    frame.Show()
    frame.Center()
    app.MainLoop()
