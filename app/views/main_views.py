from flask import Blueprint, render_template, request, redirect
from db import insert_video, get_db_connection, close_db_connection

main = Blueprint('main', __name__)

@main.route('/')
def home():
    conn = get_db_connection()
    if conn is None:
        return "Erro ao conectar com o banco de dados", 500  
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM videos ORDER BY id DESC LIMIT 6')  
    videos = cursor.fetchall()
    close_db_connection(conn)
    
    return render_template('home.html', videos=videos)  


@main.route('/episodes')
def episodes():
    conn = get_db_connection()
    if conn is None:
        return "Erro ao conectar com o banco de dados", 500  
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM videos ORDER BY id DESC')  
    videos = cursor.fetchall()
    close_db_connection(conn)
    
    return render_template('episodes.html', videos=videos)  


@main.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        video_link = request.form['video_link']
        image_path = request.form['image_path']
        title = request.form['title']  

        insert_video(title, video_link, image_path)
        
        return redirect('/admin')
    
    return render_template('admin.html')
