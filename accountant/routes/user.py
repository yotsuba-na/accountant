import sqlite3

from flask import Blueprint, request, redirect, url_for, Response

from config import DB
from accountant.sqldb.crud import Wallet
# from accountant.forms import WalletForm


app = Blueprint(
    "user",
    __name__,
    url_prefix="/user",
    static_folder="static",
)


@app.route(rule="/", methods=["POST"])
def add_wallet():
    # TODO: uncomment
    # form = WalletForm(request.form)

    # if not form.validate_on_submit():
    #     print("Not validated")
    #     # return 404

    wallet_title = request.form.get("walletTitle")
    wallet_balance = request.form.get("walletBalance")
    wallet_currency = request.form.get("walletCurrency")
    wallet_type = request.form.get("walletType")

    # TODO: use Flask-WTF
    if not all((wallet_title, wallet_balance)):
        return Response(
            response="Validation Error: Title and Balance are required!",
            status=404,
        )

    with sqlite3.connect(DB.DATABASE_FILEPATH) as conn:
        curr = conn.cursor()
        wallet_id = Wallet(curr).add(
            wallet_title, wallet_balance, wallet_currency, wallet_type
        )
        conn.commit()
    # TODO: return id

    return redirect(url_for("main.index"))
