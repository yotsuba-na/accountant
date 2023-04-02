import sqlite3

from flask import Blueprint, request
from flask import redirect, url_for, render_template

from config import DB
from accountant.sqldb import tables, crud


# XXX: VOCABULARY
# us2 = user subscribed to


app = Blueprint(
  'transaction', __name__, url_prefix='/transaction', static_folder='static'
)


@app.route('/add', methods=['POST'])
def add():
  print('>>', request.form)
  # // get the transaction
  # // crud .add
  return redirect(url_for('main.index'))


@app.route('/update', methods=['POST'])
def update():
  pass


@app.route('/delete', methods=['POST'])
def delete():
  pass
