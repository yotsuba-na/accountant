import sqlite3
from accountant.sqldb import get_db_path
from flask import Blueprint, render_template


app = Blueprint('main', __name__, url_prefix='/', static_folder='static')


def get_user_filter(cursor, user_id, object_name):
    """Gets filtered user"""
    print(f'{user_id=}')
    objids = cursor.execute(
        f'SELECT obj_ids FROM filters WHERE uid={user_id}'
    ).fetchone()

    print(f"{objids=}")
    if objids:
        return list(map(int, objids.split(',')))
    else:
        return (1, 2)


def get_filtered_users(user_id):
    return 1
    # list[user]


def get_users(cursor):
    data = cursor.execute('SELECT * FROM Users').fetchall()

    return data


def get_schedules(cursor, users_id):
    print(f'SELECT * FROM Schedule WHERE uid in {users_id}')
    schedules = cursor.execute(
        f'SELECT * FROM Schedule WHERE uid in {users_id}'
    ).fetchall()

    return schedules


def current_logged_user():
    return 1


@app.route('/')
def index():
    current_user = current_logged_user()

    with sqlite3.connect(get_db_path(app)) as conn:
        cur = conn.cursor()

        filtered_user_id = get_user_filter(cur, current_user, 'filters')
        filtered_users = get_filtered_users(cur)
        schedule = get_schedules(cur, filtered_user_id)

    return render_template('main.html')
