import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='spandana7'
)

cur=conn.cursor()

class updated:
    def dptupdate(x,colname,newval,oldval):
        cur.execute(f"update department set {colname}='{newval}' where {colname}='{oldval}'")
        conn.commit()

        
    def crs_update(self, colname, newval, oldval):
        cur.execute(f"UPDATE Course SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()

    def fclty_update(self, colname, newval, oldval):
        cur.execute(f"UPDATE Faculty SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()

    def std_update(self, colname, newval, oldval):
        cur.execute(f"UPDATE Student SET {colname} = '{newval}' WHERE {colname} = '{oldval}'")
        conn.commit()


cur.close()
conn.close()    
            
