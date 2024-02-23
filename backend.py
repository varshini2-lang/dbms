from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Replace these values with your MySQL server credentials
host = "localhost"
user = "root"
password = "arrow@7501"
database = "varshini"

# Function to establish a connection to the MySQL database
def get_database_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Function to create a 'login' table in the database if it doesn't exist

# Route to display the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_database_connection()
        cursor = connection.cursor()

        # Check if the provided username exists
        cursor.execute("SELECT * FROM login WHERE username=%s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # User already exists, render the login page with an error message
            connection.close()
            return render_template('login.html', error="Username already taken")

        # Save the new user's credentials to the 'login' table
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, hashed_password))
        connection.commit()

        connection.close()

        # Registration successful, store username in session and render a welcome message
        session['username'] = username
        return render_template('login.html', username=username)

    return render_template('login.html', error=None)

# Route to logout


if __name__ == '__main__':
    app.run(debug=True)
