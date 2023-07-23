import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='spandana7'
)

cur=conn.cursor()

class deleted:
    def dptdelete(x,dptid,dptname):
        cur.execute(f"delete form department where departmentid= {id})")
        conn.commit()

    def crs_delete(self, courseid):
        cur.execute(f"DELETE FROM Course WHERE courseid = {courseid}")
        conn.commit()

    def fclty_delete(self, facultyid):
        cur.execute(f"DELETE FROM Faculty WHERE facultyid = {facultyid}")
        conn.commit()

    def std_delete(self, sid):
        cur.execute(f"DELETE FROM Student WHERE sid = {sid}")
        conn.commit()


cur.close()
conn.close()        