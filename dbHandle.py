import cx_Oracle as o

try:
    dsn = o.makedsn('192.168.99.100','1521','xe')
    #dsn = o.makedsn('호스트 이름','포트','SID')
    conn = o.connect(user='hr',password='hr',dsn=dsn)
    #cur = conn.cursor()
    print("oracle connect")
except Exception as err:
    print('err:',err)

#======================

def insertinfo(name, age, loca):
    try:
        sql="insert into table1 values(:name, :age, :location)" #SQL 형식
        dsn=o.makedsn('192.168.99.100','1521','xe')
        conn=o.connect(user="hr",password="hr",dsn=dsn)
        cur=conn.cursor()
        cur.execute(sql, (name,int(age),loca))

        conn.commit()
        conn.close

        return "<h1> insert success<h1>"
    except Exception as err:
        print('err:', err)

        return "<h1> insert fail<h1>"




