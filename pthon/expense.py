from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "user1": "password123",
    "user2": "mysecurepassword"
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if users.get(username) == password:
        return redirect(url_for('main'))
    else:
        return render_template('login.html', error="Invalid credentials")

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
