from flask import Blueprint, render_template


app = Blueprint('main', __name__, url_prefix='/', static_folder='static')


@app.route('/')
def index():
  return render_template('main.html')
