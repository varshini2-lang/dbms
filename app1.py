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
def show_music():
    connection = get_database_connection()
    cursor = connection.cursor()

    # Retrieve data from the music table
    cursor.execute("SELECT * FROM music")
    music_data = cursor.fetchall()

    connection.close()

    return render_template('index.html', music_data=music_data)

# Route to insert new data into the music table
@app.route('/add_song', methods=['POST'])
def add_song():
    title = request.form['title']
    artist = request.form['artist']
    album = request.form['album']
    year = request.form['year']

    connection = get_database_connection()
    cursor = connection.cursor()

    # Insert new data into the music table
    cursor.execute("INSERT INTO music (title, artist, album, year) VALUES (%s, %s, %s, %s)",
                   (title, artist, album, year))
    connection.commit()

    connection.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
