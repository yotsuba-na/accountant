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

  owner_id = 1
  parent_id = None
  title = request.form.get('transactionTitle')
  status = request.form.get('transactionStatus')
  type_id = request.form.get('transactionType')
  function_id = 1
  wallet_id = 1
  currency_id = 1
  value = request.form.get('transactionValue')

  if all((title, value)):
    # data = {
    #   'owner_id': 1,
    #   'parent_id': parent_id,
    #   'title': title,
    #   'status': status,
    #   'type_id': type_id,
    #   'function_id': function_id,
    #   'wallet_id': wallet_id,
    #   'currency_id': currency_id,
    #   'value': value
    # }
    with sqlite3.connect(DB.FILEPATH) as conn:
      curr = conn.cursor()
      crud.Transaction(curr).add(owner_id, form)
      conn.commit()

  # // get the transaction
  # // crud .add
  return redirect(url_for('main.index'))


@app.route('/update', methods=['POST'])
def update():
  pass


@app.route('/delete', methods=['POST'])
def delete():
  pass
