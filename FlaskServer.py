from flask import Flask, render_template, request
import cx_Oracle as o

app=Flask(__name__) # 시작

@app.route("/") # 해당 홈페이지로 이동
def rootFn():
    return "hello flask" # 해당하는 값 출

@app.route("/a")
def mainFn():
    return render_template('a.html') #html 문서를 불러옴

@app.route("/b") # 홈페이지 뒷부분에 작성
def addrprocFn():
    myname =request.args['myname'] # 해당 변수값을 요구
    myage =request.args['myage']
    myaddr =request.args['myaddr']
    s=f'이름:{myname} 나이:{myage} 주소:{myaddr}' # 포맷함수
    return s #html 문서를 불러

 #=====DB에 데이터 넣기===========
@app.route("/test_info")
def test_infoFn():
    return render_template('test_info.html') #html 문서를 불러옴

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

@app.route("/test_insertinfo")
def test_insertinfoFn():
    myname=request.args['myname']
    myage=request.args['myage']
    myloca=request.args['myloca']
    rst = insertinfo(myname,myage,myloca)
    return rst

@app.route("/selectinfo")
def selectinfoFn():
    data = selectinfoFn()
    return render_template("selectinfo.html", stdData=data)


if __name__ == '__main__':
    app.run(debug=True) # 끝
