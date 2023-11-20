from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def page_navigation():
    return render_template('navigation.html')

@app.route("/page1") 
def page_1():
    return render_template('page1.html')
@app.route("/page2")     
def page_2():
    return render_template('page2.html')
if __name__=='__main__':
    app.run(host='0.0.0.0',port='5004',debug=True)
