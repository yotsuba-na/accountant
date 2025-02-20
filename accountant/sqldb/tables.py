import pathlib
import sqlite3


__all__ = ("db_create_all",)


class Transaction:
    def __init__(self, curr):
        self.curr = curr

    def transaction(self):
        self.curr.execute(
            # status: planned, fact
            """
      CREATE TABLE IF NOT EXISTS `transaction` (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id    INTEGER,
        parent_id   INTEGER,
        title       VARCHAR (50),
        status      VARCHAR (10),
        type_id     INTEGER,
        function_id INTEGER,
        wallet_id   INTEGER,
        currency_id INTEGER,
        value       DECIMAL (10, 2),
        created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at  DATETIME
      )
      """
        )

    def transaction_type(self):
        # types: {'regular', 'schedule', 'transfer'}
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS transaction_type (
              id          INTEGER PRIMARY KEY AUTOINCREMENT,
              type        VARCHAR (10) NOT NULL
            )
            """
        )

        transaction_types = self.curr.execute(
            "SELECT * FROM transaction_type"
        ).fetchone()
        if not transaction_types:
            self.curr.executemany(
                "INSERT INTO transaction_type (type) VALUES (?)",
                (
                    ("regular",),
                    ("schedule",),
                    ("transfer",),
                ),
            )

    def transaction_function(self):
        # funcs: {'increment', 'decrement'}
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS transaction_function (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                func        VARCHAR (10) NOT NULL
            )
            """
        )

    def create_all(self):
        self.transaction()
        self.transaction_type()
        self.transaction_function()


class TransactionTransfer:
    def __init__(self, curr):
        self.curr = curr

    def transaction_transfer(self):
        # obj_names: {'user', 'currency'}
        self.curr.execute(
            """
      CREATE TABLE IF NOT EXISTS transaction_transfer (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id        INTEGER,
        transaction_id  INTEGER,
        transfer_from   INTEGER,
        transfer_to     INTEGER,
        currency_id     INTEGER,
        value           DECIMAL (10, 2) NOT NULL
      )
      """
        )

    def create_all(self):
        self.transaction_transfer()


class User:
    def __init__(self, curr):
        self.curr = curr

    def user(self):
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname    VARCHAR(50),
                currency_id INTEGER
            )
            """
        )

    def create_all(self):
        self.user()


class Currency:
    def __init__(self, curr):
        self.curr = curr

    def currency(self):
        """USD, CNY, JPY, RUB"""
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS currency (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                currency    VARCHAR (10),
                value       DECIMAL (10, 2),
                created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at
            )
            """
        )

        # TODO: rename *currency to *code
        has_currencies = self.curr.execute("SELECT * FROM currency").fetchone()
        if not has_currencies:
            self.curr.executemany(
                "INSERT INTO currency (currency, value) VALUES (?, ?)",
                (
                    ("jpy", 1),
                    ("usd", 1),
                    ("rub", 1),
                ),
            )

    def create_all(self):
        self.currency()


class Wallet:
    def __init__(self, curr):
        self.curr = curr

    def wallet(self):
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS wallet (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       VARCHAR (50),
                owner_id    INTEGER,
                balance     DECIMAL (10, 2),
                currency_id INTEGER,
                type_id     INTEGER
            )
            """
        )

    def wallet_type(self):
        # types: {'linked', 'shared', 'temporary'}
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS wallet_type (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                type        VARCHAR (10)
            )
            """
        )

        has_types = self.curr.execute("SELECT * FROM wallet_type").fetchone()
        if not has_types:
            self.curr.executemany(
                "INSERT INTO wallet_type (`type`) VALUES (?)",
                (
                    ("linked",),
                    ("shared",),
                    ("temporary",),
                ),
            )

    def create_all(self):
        self.wallet()
        self.wallet_type()


class Filters:
    def __init__(self, curr):
        self.curr = curr

    def filters(self):
        # obj_names: {'user', 'currency'}
        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS filters (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id    INTEGER,
                obj_name    VARCHAR (10),
                obj_ids     TEXT NOT NULL
            )
            """
        )

    def create_all(self):
        self.filters()


def db_create_all(DB_FILEPATH: pathlib.Path) -> None:
    with sqlite3.connect(DB_FILEPATH) as conn:
        curr = conn.cursor()

        Transaction(curr).create_all()
        TransactionTransfer(curr).create_all()
        User(curr).create_all()
        Currency(curr).create_all()
        Wallet(curr).create_all()
        Filters(curr).create_all()

        conn.commit()
