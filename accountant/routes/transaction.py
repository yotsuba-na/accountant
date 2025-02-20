import sqlite3

from flask import Blueprint, request
from flask import redirect, url_for, render_template

from config import DB
from accountant.sqldb import tables, crud
from accountant.forms import TransactionForm


app = Blueprint(
  'transaction', __name__, url_prefix='/transaction', static_folder='static'
)


# TODO: Make it REST


@app.route('/add', methods=['POST'])
def add():
  form = TransactionForm(request.form)

  if not form.validate_on_submit():
    return 404

  with sqlite3.connect(DB.DATABASE_FILEPATH) as conn:
    curr = conn.cursor()
    crud.Transaction(curr).add(owner_id, form)
    conn.commit()

  return redirect(url_for('main.index'))


@app.route('/update', methods=['POST'])
def update():
  pass


@app.route('/delete', methods=['POST'])
def delete():
  pass
