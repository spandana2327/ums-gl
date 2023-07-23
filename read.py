import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='spandana7'
)

cur=conn.cursor()

class reading:
    def dptread(x,dptid,dptname):
        cur.execute(f"select* form department where departmentid= {id})")
        print(cur.fetchall())

    def crs_read(self, courseid):
        cur.execute(f"SELECT * FROM Course WHERE courseid = {courseid}")
        print(cur.fetchall())

    def fclty_read(self, facultyid):
        cur.execute(f"SELECT * FROM Faculty WHERE facultyid = {facultyid}")
        print(cur.fetchall())

    def std_read(self, sid):
        cur.execute(f"SELECT * FROM Student WHERE sid = {sid}")
        print(cur.fetchall())

cur.close()
conn.close()        

        