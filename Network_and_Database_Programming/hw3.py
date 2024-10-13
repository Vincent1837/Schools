import wx
import MySQLdb

# 連接 SQLite 資料庫
conn = MySQLdb.Connection(host='127.0.0.1', user='root', port=3306, db='test', password='ag061837')
cursor = conn.cursor()

# 建立資料表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT (
        SID VARCHAR(10) PRIMARY KEY,
        Fname VARCHAR(100),
        Lname VARCHAR(100),
        Grade INT,
        Sex VARCHAR(10),
        Email VARCHAR(100)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS COURSE (
        CID VARCHAR(10) PRIMARY KEY,
        Cname VARCHAR(100)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS REMINDER (
        SID VARCHAR(10),
        CID VARCHAR(10),
        PRIMARY KEY (SID, CID)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ENROLLMENT (
        SID VARCHAR(10),
        CID VARCHAR(10),
        MidScore INT DEFAULT 0,
        FinalScore INT DEFAULT 0,
        PRIMARY KEY (SID, CID)
    );
''')

""" cursor.execute('''
    DROP TRIGGER IF EXISTS `test`.`Reminder_Trigger`;

    DELIMITER $$
    USE `test`$$
    CREATE DEFINER = CURRENT_USER TRIGGER `test`.`Reminder_Trigger` AFTER UPDATE ON `enrollment` FOR EACH ROW
    BEGIN
        IF NEW.MidScore < 60 THEN
            INSERT INTO REMINDER (SID, CID) VALUES (NEW.SID, NEW.CID);
        END IF;
    END;$$
    DELIMITER ;
''') """

conn.commit()

# 主窗口框架
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
        
        # 輸入期中成績
        self.midterm_panel = wx.Panel(notebook)
        self.enter_midterm_score(self.midterm_panel)
        notebook.AddPage(self.midterm_panel, "輸入期中成績")
        
        # 發送預警郵件
        self.reminder_panel = wx.Panel(notebook)
        self.send_reminder_email(self.reminder_panel)
        notebook.AddPage(self.reminder_panel, "發送預警郵件")
        
        # 輸入期末成績
        self.final_panel = wx.Panel(notebook)
        self.create_enrollment_panel(self.final_panel)
        notebook.AddPage(self.final_panel, "輸入期末成績")

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
        self.grade_rbox = wx.RadioBox(panel, label="年級", choices=['1', '2', '3', '4','5', '6'])
        self.sex_rbox = wx.RadioBox(panel, label="性別", choices=['男', '女'])
        self.email_txt = wx.TextCtrl(panel)
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
        vbox.Add(submit_btn1, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)

    def on_add_student(self, event):
        sid = self.sid_txt.GetValue()
        fname = self.fname_txt.GetValue()
        lname = self.lname_txt.GetValue()
        grade = self.grade_rbox.GetStringSelection()
        sex = self.sex_rbox.GetStringSelection()
        email = self.email_txt.GetValue()

        cursor.execute(f"INSERT INTO STUDENT (SID, Fname, Lname, Grade, Sex, Email) VALUES ('{sid}', '{fname}', '{lname}', {grade}, '{sex}', '{email}')")
        conn.commit()
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

        cursor.execute(f"INSERT INTO COURSE (CID, Cname) VALUES ('{cid}', '{cname}')")
        conn.commit()
        wx.MessageBox(f"課程 {cname} 已新增", "訊息", wx.OK | wx.ICON_INFORMATION)

    # 新增選課資料區塊
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
        print(sid, ',', cid)
        cursor.execute(f"INSERT INTO ENROLLMENT (SID, CID) VALUES ('{sid}', '{cid}')")
        conn.commit()
        wx.MessageBox(f"選課資料已新增", "訊息", wx.OK | wx.ICON_INFORMATION)

    # 輸入期中成績
    def enter_midterm_score(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sid_midterm_txt = wx.TextCtrl(panel)
        self.cid_midterm_txt = wx.TextCtrl(panel)
        self.midterm_score_txt = wx.TextCtrl(panel)
        submit_btn4 = wx.Button(panel, label="輸入期中成績")
        submit_btn4.Bind(wx.EVT_BUTTON, self.on_add_mid)

        vbox.Add(wx.StaticText(panel, label="學號"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.sid_midterm_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="課程號碼"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cid_midterm_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="期中成績"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.midterm_score_txt, flag=wx.EXPAND | wx.ALL, border=5)
        
        vbox.Add(submit_btn4, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)

    def on_add_mid(self, event):
        sid = self.sid_midterm_txt.GetValue()
        cid = self.cid_midterm_txt.GetValue()
        mid = self.midterm_score_txt.GetValue()
        cursor.execute(f"UPDATE ENROLLMENT set MidScore = {mid} WHERE SID = '{sid}' AND CID = '{cid}'")
        conn.commit()
        wx.MessageBox(f"期中成績已新增", "訊息", wx.OK | wx.ICON_INFORMATION)
        
    # 發送預警郵件
    def send_reminder_email(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)
        stds = []
        cursor.execute('SELECT * FROM REMINDER')
        
        send_button = wx.Button(panel, label="發送預警郵件")
        send_button.Bind(wx.EVT_BUTTON, self.on_send_pushed)
        
        vbox.Add(send_button, flag=wx.EXPAND | wx.ALL, border=5)
        
        
    def on_send_pushed(self, event):
        cursor.execute('SELECT * FROM REMINDER')
        for _ in cursor.fetchall():
            print(_)
    
    
    
    
    
    
    # 輸入期末成績
    def enter_final_score(self, panel):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.sid_final_txt = wx.TextCtrl(panel)
        self.cid_final_txt = wx.TextCtrl(panel)
        self.final_score_txt = wx.TextCtrl(panel)
        submit_btn5 = wx.Button(panel, label="輸入期末成績")
        submit_btn5.Bind(wx.EVT_BUTTON, self.on_submit5_pressed)
        
        vbox.Add(wx.StaticText(panel, label="學號"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.sid_final_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="課程號碼"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cid_final_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="期末成績"), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.final_score_txt, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(submit_btn5, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)
        
    def on_submit5_pressed(self, event):
        sid = self.sid_final_txt.GetValue()
        cid = self.cid_final_txt.GetValue()
        final = self.final_score_txt.GetValue()
        
        cursor.execute(f"UPDATE ENROLLMENT SET FinalScore = {final} WHERE SID = '{sid}' AND CID = '{cid}'")
        conn.commit()
        wx.MessageBox(f"期末成績已新增", "訊息", wx.OK | wx.ICON_INFORMATION)
        
    
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
        cursor.execute('''
            SELECT STUDENT.SID, STUDENT.Fname, STUDENT.Lname, 
            (0.4 * ENROLLMENT.MidScore + 0.6 * ENROLLMENT.FinalScore) as TotalScore 
            FROM ENROLLMENT 
            JOIN STUDENT ON ENROLLMENT.SID = STUDENT.SID
            WHERE ENROLLMENT.CID = ?
        ''', (cid,))
        
        results = cursor.fetchall()
        result_str = "\n".join([f"{row[0]} {row[1]} {row[2]}: {row[3]:.2f}" for row in results])
        wx.MessageBox(f"成績:\n{result_str}", "總成績", wx.OK | wx.ICON_INFORMATION)

# 啟動程式
if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, "學生管理系統")
    frame.Show()
    frame.Center()
    app.MainLoop()

    # 關閉資料庫連線
    conn.close()
