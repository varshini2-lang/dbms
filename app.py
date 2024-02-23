import mysql.connector

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

# Function to create tables in the database
def create_tables():
    connection = get_database_connection()
    cursor = connection.cursor()

    # Creating a table for the music library
    create_music_table_query = """
    CREATE TABLE IF NOT EXISTS music (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        artist VARCHAR(255) NOT NULL,
        album VARCHAR(255) NOT NULL,
        year INT
    )
    """

    # Creating a table for user login
    create_login_table_query = """
    CREATE TABLE IF NOT EXISTS login (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """

    cursor.execute(create_music_table_query)
    cursor.execute(create_login_table_query)

    # You can add more create table queries here for additional tables

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_tables()
    print("Tables created successfully.")
