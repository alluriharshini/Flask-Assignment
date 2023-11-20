from flask import Flask, request, render_template
app=Flask(__name__)

@app.route('/uploadfile')
def upload_file():
    return render_template('uploadfile.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        file.save("uploads/" + file.filename)
        return "File uploaded successfully"

if __name__=='__main__':
    app.run(host='0.0.0.0',port='5003',debug=True) 
