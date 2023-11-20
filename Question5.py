from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key

@app.route('/')
def home():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']
        return f"Welcome, {username}! <a href='/logout'>Logout</a>"
    return "Welcome to the Flask app with user sessions. <a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Store the username in the session
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('question5.html')

@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5004',debug=True)
