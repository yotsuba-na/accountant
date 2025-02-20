from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class WalletForm(FlaskForm):
    class Meta:
        csrf = False

    wallet_title = StringField("walletTitle", validators=[DataRequired()])
    wallet_balance = FloatField("walletBalance", validators=[DataRequired()])
    # TODO: choices
    wallet_currency = StringField(
        "walletCurrency",
        validators=[DataRequired()],
    )
    # TODO: choices
    wallet_type = StringField("walletType", validators=[DataRequired()])


class TransactionForm(FlaskForm):
    class Meta:
        csrf = False

    parent_id = IntegerField("parent_id")
    name = StringField("name", validators=[DataRequired()])
    title = StringField("title", validators=[DataRequired()])
    status = StringField("status", validators=[DataRequired()])
    type_id = IntegerField("type_id", validators=[DataRequired()])
    function_id = IntegerField("function_id", validators=[DataRequired()])
    wallet_id = IntegerField("wallet_id", validators=[DataRequired()])
    currency_id = IntegerField("currency_id", validators=[DataRequired()])
    value = IntegerField("value", validators=[DataRequired()])
    transaction_from = IntegerField("transaction_from")
    transaction_to = IntegerField("transaction_to")
