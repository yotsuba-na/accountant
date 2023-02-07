import sqlite3
from accountant.sqldb import tables, query
from flask import Blueprint, render_template


app = Blueprint('main', __name__, url_prefix='/', static_folder='static')


def current_logged_user():
    return 1


@app.route('/', methods=['GET'])
def index():
    current_user = current_logged_user()

    with sqlite3.connect(tables.get_db_path(app)) as conn:
      curr = conn.cursor()

      user_subscription = query.Filters(curr).get_user_filter(
        current_user, 'user'
      )
      all_users = query.User(curr).get_all()
      users_schedules = query.Schedules(curr).get_users_schedules(
        user_subscription
      )
      users_todo = query.Todo(curr).get_users_todo(
        user_subscription
      )

    return render_template(
      'main.html',
      user_subscription=user_subscription,
      all_users=all_users,
      users_schedules=users_schedules,
      users_todo=users_todo
    )
