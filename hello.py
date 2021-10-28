from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
 
@app.route('/userLogin', methods = ['POpyST'])
def userLogin():
    user = request.get_json()#json 데이터를 받아옴
    return jsonify(user)# 받아온 데이터를 다시 전송
 
@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})
 
if __name__ == "__main__":
    app.run()