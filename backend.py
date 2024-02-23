from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

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

# Route to display the music library
@app.route('/')
def show_login():
    connection = get_database_connection()
    cursor = connection.cursor()

    # Retrieve data from the music table
    cursor.execute("SELECT * FROM login")
    music_data = cursor.fetchall()

    connection.close()

    return render_template('login.html')

# Route to insert new data into the music table
@app.route('/login', methods=['POST'])
def add_song():
    username = request.form['username']
    password = request.form['password']

    connection = get_database_connection()
    cursor = connection.cursor()

    # Insert new data into the music table
    cursor.execute("INSERT INTO login (username,password) VALUES (%s, %s)",
                   (username,password))
    connection.commit()

    connection.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
