from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('home.html')

@main.route('/episodes')
def episodes():
  return render_template('episodes.html')
