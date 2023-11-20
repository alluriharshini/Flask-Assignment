from flask import Flask,request

app=Flask(__name__)


@app.route('/user')
def user_name():
    data=request.args.get('name')
    return f"{data}"

if __name__=='__main__':
    app.run(host="0.0.0.0",port='5009')    

