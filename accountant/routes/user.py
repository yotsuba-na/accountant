from flask import Blueprint, render_template


app = Blueprint('user', __name__, url_prefix='/user', static_folder='static')
