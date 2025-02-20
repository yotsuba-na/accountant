import sqlite3

from flask import Blueprint, request
from flask import redirect, url_for, render_template

from config import DB
from accountant.sqldb import tables, crud
from accountant.forms import TransactionForm


app = Blueprint('main', __name__, url_prefix='/', static_folder='static')


def current_logged_user():
    return 1


@app.route('/', methods=['GET', 'POST'])
def index():
    current_user = current_logged_user()
    if request.method == "POST":
        main_form_data = request.form.get("mainFormData")

    with sqlite3.connect(DB.DATABASE_FILEPATH) as conn:
        curr = conn.cursor()

        us2_users = crud.Filter(curr).get(user_id=current_user, obj_name="user")
        all_users = crud.User(curr).get_all()
        users_transactions = crud.Transaction(curr).get_all(users_id=us2_users)
        all_currencies = crud.Currency(curr).get_all()
        us2_currencies = crud.Filter(curr).get(
            user_id=current_user, obj_name="currency"
        )
        all_wallets = crud.Wallet(curr).get_all()
        all_transactions = crud.Transaction(curr).get_all()
        all_transaction_types = crud.TransactionType(curr).get_all()

    return render_template(
        "main.html",
        us2_users=us2_users,
        all_users=all_users,
        users_transactions=users_transactions,
        all_currencies=all_currencies,
        us2_currencies=us2_currencies,
        all_wallets=all_wallets,
        all_transactions=all_transactions,
        all_transaction_types=all_transaction_types,
        transaction_form=TransactionForm(),
    )
