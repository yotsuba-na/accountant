def list_to_query_str(target: list) -> str:
    if len(target) == 1:
        return f"({target[0]})"
    return str(tuple(target))


class User:
    """Query for `user` table"""

    def __init__(self, curr):
        self.curr = curr

    def get_all(self, by_ids: list[int] | None = None) -> list:
        query = "SELECT * FROM user"

        if by_ids is not None:
            query += f" WHERE id IN {list_to_query_str(by_ids)}"

        return self.curr.execute(query).fetchall()


class Filter:
    """Query for `filters` table"""

    def __init__(self, curr):
        self.curr = curr

    def get(self, user_id: int, obj_name: str) -> list:
        """Gets user filter for `obj_name` table"""
        obj_ids = self.curr.execute(
            f"""
            SELECT obj_ids FROM filters
            WHERE owner_id={user_id} AND obj_name='{obj_name}'
            """
        ).fetchone()

        if obj_ids is not None:
            obj_ids = list(map(int, obj_ids.split(",")))

        return obj_ids


class TransactionType:
    def __init__(self, curr):
        self.curr = curr

    # TODO: REMOVE: use *get_all instead
    def get(self, type_id: int):
        return self.curr.execute(
            "SELECT `type` FROM transaction_type WHERE id = ?",
            (type_id,),
        )

    def get_all(self, types_id: list[int] | None = None):
        query = "SELECT * FROM transaction_type"

        if types_id is not None:
            query += f" WHERE id IN {list_to_query_str(types_id)}"

        return self.curr.execute(query).fetchall()


class TransactionTransfer:
    def __init__(self, curr):
        self.curr = curr

    def add(
        self,
        user_id: int,
        transaction_id: int,
        data: dict,
    ) -> int:
        transfer_id = self.curr.execute(
            """
        INSERT INTO transaction_transfer (
            owner_id, transaction_id,
            transfer_from, transfer_to, currency_id, value
        ) VALUES (
            ?, ?, ?, ?, ?
        )
        """,
            (
                data[c]
                for c in (
                    "owner_id",
                    "transaction_id",
                    "transfer_from",
                    "transfer_to",
                    "currency_id",
                    "value",
                )
            ),
        )
        self.curr.commit()


class Transaction:
    """Query for `transaction` table"""

    def __init__(self, curr):
        self.curr = curr

    def _add_transfer(user_id: int, data: dict):
        pass

    def add(self, user_id: int, data: dict) -> int:
        query = """
        INSERT INTO `transaction` (
        owner_id, parent_id, title, status,
        type_id, function_id, wallet_id, currency_id, value
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = [
            data[c]
            for c in (
                "owner_id",
                "parent_id",
                "title",
                "status",
                "type_id",
                "function_id",
                "wallet_id",
                "currency_id",
                "value",
            )
        ]

        self.curr.execute(query, values)
        transaction_id = self.curr.lastrowid

        transaction_type = TransactionType(self.curr).get(
            data["type_id"],
        )
        if transaction_type == "transfer":
            TransactionTransfer(self.curr).add(
                user_id,
                transaction_id,
                data,
            )

        return transaction_id

    def get_all(self, users_id: list[int] | None = None):
        """Transactions (can be filtered by `users_id`)"""
        query = "SELECT * FROM `transaction`"

        if users_id is not None:
            query += f" WHERE owner_id IN {list_to_query_str(users_id)}"

        return self.curr.execute(query).fetchall()


class Currency:
    """Query for `currency` table"""

    def __init__(self, curr):
        self.curr = curr

    def get_all(self, by_ids: list[int] | None = None) -> list:
        query = "SELECT * FROM currency"

        if by_ids is not None:
            query += f" WHERE id IN {list_to_query_str(by_ids)}"

        return self.curr.execute(query).fetchall()


class Wallet:
    """Query for `wallet` table"""

    def __init__(self, curr):
        self.curr = curr

    def add(
        self,
        title: str,
        balance: int,
        currency: str,
        type_: str,
    ) -> int:
        # TODO: use func
        type_id = self.curr.execute(
            "SELECT id FROM wallet_type WHERE `type` = ?", (type_,)
        ).fetchone()[0]

        # TODO: use func
        currency_id = self.curr.execute(
            "SELECT id FROM currency WHERE currency = ?",
            (currency,),
        ).fetchone()[0]

        self.curr.execute(
            "INSERT INTO wallet (title, balance, currency_id, type_id) VALUES (?, ?, ?, ?)",
            (title, balance, currency_id, type_id),
        )

        return self.curr.lastrowid

    def get_all(self, by_ids: list[int] | None = None) -> list:
        query = "SELECT * FROM wallet"

        if by_ids is not None:
            query += f" WHERE id IN {list_to_query_str(by_ids)}"

        return self.curr.execute(query).fetchall()
