from flask import Flask, render_template, redirect, url_for, flash, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

# Dummy user database for demonstration purposes
users = {
    'user1': {'password': generate_password_hash('password1')},
    'user2': {'password': generate_password_hash('password2')}
}

@app.route('/')
def home():
    return 'Home Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Logged in successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'password': generate_password_hash(password)}
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Choose a different username.', 'danger')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
