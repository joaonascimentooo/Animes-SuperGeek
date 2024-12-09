import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Altere de acordo com seu Usuario
            password='root',  # Altere de acordo com sua SEnha
            database='animessupergeek'  # Altere para o nome do seu Banco
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Não Conectou ao Banco: {e}")
        return None

def close_db_connection(connection):
    if connection and connection.is_connected():
        connection.close()

def insert_video(title, video_link, image_path):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO videos (title, video_link, image_path) VALUES (%s, %s, %s)', 
            (title, video_link, image_path)
        )
        connection.commit()
        close_db_connection(connection)
