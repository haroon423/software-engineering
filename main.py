from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy in-memory database for storing user information
users = {
    'user1': {'username': 'user1', 'password': 'password1'},
    'user2': {'username': 'user2', 'password': 'password2'}
}

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            # Successful login
            return f"Logged in as {username}"
        else:
            # Invalid username or password
            return "Invalid username or password"

    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
