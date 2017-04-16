import pymysql


def check_login(username, password):
    connect()
    # sql='''SELECT username,password from Users where username=%s and password = %s'''
    # cursor = db.cursor()
    # cursor.execute( sql,(self.use1.get(),self.p1.get()))
    # db.close()
    # if cursor.execute =='':

    # messagebox.showerror('Login failed',"Check username and password")
    # return

    print("CHECKING LOGIN")


def connect():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='cheape42', db='mysql')

    cur = conn.cursor()

    cur.execute("SELECT Host,User FROM user")


def register():
    self.connect()
    user = nm4.get()
    fullname = nm3.get()
    passwd = ps3.get()
    confirm = ps4.get()
    digits = '0123456789'
    dig = 0
    Up = 0
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if user == '':
        messagebox.showerror('Error', "Registration Failed: Empty User name")
    return
    if user == '''SELECT username from GTChatUsers where username = user''':
        messagebox.showerror('Error', "Registration Failed: Username taken")
        return
    if passwd != confirm:
        messagebox.showerror(
            'Error', "Registration Failed: Password does not mach confirmation")
        return
    for x in passwd:
        if x in digits:
            dig = dig + 1
        elif x in upper:
            Up = Up + 1
    if dig == 0 or Up == 0:
        messagebox.showerror(
            'Error', "Registration Failed: Password needs 1 capital letter and 1 number")
        return
        
    toLoginwin()
    sql = '''INSERT INTO GTChatUsers (username,fullname,password) VALUES (%s,%s,%s)'''
    cursor2 = self.db.cursor()
    cursor2.execute(sql, (nm4.get(), nm3.get(), ps3.get()))
    db.commit()
    db.close()
