# login.py
 
from flask import *  
# Flask 인스턴스 생성
app = Flask(__name__) 
 
 
@app.route('/')
def hello():
    return render_template('login.html')
 
 
# login 주소에서 POST 방식의 요청을 받았을 때
@app.route('/login',methods = ['POST'])  
def login():  
    id = request.form['id']  
    passwrd = request.form['pass'] 
 
    if id=="Elice" and passwrd=="Awesome!": 
        return "Welcome %s" % id  
 
 
if __name__ == '__main__':  
    app.run()