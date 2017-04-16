from app import app
import pymysql

def check_login(username, password):
      connect()
      sql='''SELECT username,password from GTChatUsers where username=%s and password = %s'''
      cursor = self.db.cursor()
      cursor.execute( sql,(self.use1.get(),self.p1.get()))
      db.close()
      if cursor.execute =='':
     
       messagebox.showerror('Login failed',"Check username and password")
       return
    
    print("CHECKING LOGIN");
