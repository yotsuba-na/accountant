import sqlite3
from accountant.sqldb import tables, query
from flask import Blueprint, render_template


app = Blueprint('main', __name__, url_prefix='/', static_folder='static')


def current_logged_user():
    return 1


@app.route('/', methods=['GET'])
def index():
  current_user = current_logged_user()

  # XXX: VOCABULARY
  # us2 = user subscribed to
  with sqlite3.connect(tables.get_db_path(app)) as conn:
    curr = conn.cursor()

    us2_users = query.Filter(curr).get_user_filter(
      current_user, 'user'
    )
    all_users = query.User(curr).get_all()
    users_schedules = query.Schedules(curr).get_users_schedules(
      us2_users
    )
    users_todos = query.Todo(curr).get_users_todo(
      us2_users
    )
    all_currencies = query.Currency(curr).get_all()
    us2_currencies = query.Filter(curr).get_user_filter(
      current_user, 'currency'
    )
    all_wallets = query.Wallet(curr).get_all()

  return render_template(
    'main.html',
    us2_users=us2_users,
    all_users=all_users,
    users_schedules=users_schedules,
    users_todos=users_todos,
    all_currencies=all_currencies,
    us2_currencies=us2_currencies,
    all_wallets=all_wallets
  )
