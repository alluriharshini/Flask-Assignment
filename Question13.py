from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Store messages in memory for simplicity (in a real app, you might use a database)
messages = []


@app.route('/')
def index():
    return render_template('index_13.html')


@app.route('/get_messages')
def get_messages():
    timestamp = float(request.args.get('timestamp', 0))
    new_messages = [msg for msg in messages if msg['timestamp'] > timestamp]

    if not new_messages:
        # If no new messages, simulate a long poll by sleeping for a short time
        time.sleep(1)

    return jsonify(new_messages)


@app.route('/send_message', methods=['POST'])
def send_message():
    content = request.json['content']
    timestamp = time.time()
    message = {'content': content, 'timestamp': timestamp}
    messages.append(message)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
