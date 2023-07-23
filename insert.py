
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='spandana7'
)

cur=conn.cursor()

class inserted:
    def dptinsert(x,dptid,dptname):
        cur.execute(f"insert into department values({dptid},'{dptname}')")
        conn.commit()

    def crs_insert(self, courseid, coursename, coursefee, duration):
        cur.execute(f"INSERT INTO Course VALUES ({courseid}, '{coursename}', {coursefee}, {duration})")
        conn.commit()

    def fclty_insert(self, facultyid, facultyname, departmentid, salary, courseid):
        cur.execute(f"INSERT INTO Faculty VALUES ({facultyid}, '{facultyname}', {departmentid}, {salary}, {courseid})")
        conn.commit()

    def std_insert(self, sid, sname, courseid, departmentid):
        cur.execute(f"INSERT INTO Student VALUES ({sid}, '{sname}', {courseid}, {departmentid})")
        conn.commit()


cur.close()
conn.close()        