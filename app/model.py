from app import app
import pymysql

def check_login(username, password):
      connect()
      sql='''SELECT username,password from Users where username=%s and password = %s'''
      cursor = db.cursor()
      cursor.execute( sql,(self.use1.get(),self.p1.get()))
      db.close()
      if cursor.execute =='':
     
      messagebox.showerror('Login failed',"Check username and password")
       return
    
    print("CHECKING LOGIN");

def connect():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='mysql')

    cur = conn.cursor()

    cur.execute("SELECT Host,User FROM user")
