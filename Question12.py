from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_time.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    time.sleep(1)  # Simulate some processing time
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
