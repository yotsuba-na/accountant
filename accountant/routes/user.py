import sqlite3

from flask import Blueprint, render_template, request, redirect, url_for

from config import DB
from accountant.sqldb.crud import Wallet


app = Blueprint('user', __name__, url_prefix='/user', static_folder='static')


@app.route('/', methods=['POST'])
def add_wallet() -> int:
  wallet_title = request.form.get("walletTitle")
  wallet_balance = request.form.get("walletBalance")
  wallet_currency = request.form.get("walletCurrency")
  wallet_type = request.form.get("walletType")

  # TODO: use Flask-WTF
  if not all((wallet_title, wallet_balance)):
    return 404

  with sqlite3.connect(DB.DATABASE_FILEPATH) as conn:
    curr = conn.cursor()
    wallet_id = Wallet(curr).add(
      wallet_title, wallet_balance, wallet_currency, wallet_type
    )
    conn.commit()
    # TODO: return id

  return redirect(url_for('main.index'))
