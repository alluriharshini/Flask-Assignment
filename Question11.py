from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages in memory
messages = []

@app.route('/')
def index():
    #calling HTML script 
    return render_template('index_no_socketio.html')

#this will accept the html POST req
@app.route('/send_message', methods=['POST'])
def send_message():
    content = request.form['content']
    messages.append(content)
    return jsonify({'message': content})

#this will accept the html gets message from someone using the url
@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
