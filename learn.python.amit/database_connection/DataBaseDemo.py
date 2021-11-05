import cx_Oracle
class Students:
    def connectWithDb(self):
        conn=None
        try:
            conn=cx_Oracle.connect("amit_owner/abcd1234@//localhost:1521/xe")
            print(conn.version)
            cur=conn.cursor()
            sql_read="""select * from emp"""
            cur.execute(sql_read)
            for i in cur:
                print(i)
            #also we can store data in a variable
            cur.execute(sql_read)
            result=cur.fetchall() #fetchone()
            for i in result:
                print(i)
        except Exception as e:
            print("error occurred ",e)
        finally:
            pass

obj=Students()
obj.connectWithDb()

