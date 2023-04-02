import sqlite3
from os.path import join
import os

from flask import url_for


__all__ = ('db_create_all', 'get_db_path')


class Transaction:
  def __init__(self, curr):
    self.curr = curr

  def transaction(self):
    self.curr.execute(
      """
      CREATE TABLE IF NOT EXISTS `transaction` (
        id          INTEGER,
        owner_id    INTEGER,
        parent_id   INTEGER,
        title       VARCHAR (50),
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
    # types: {'planned', 'fact', 'scheduled', 'transfer'}
    self.curr.execute(
      """
      CREATE TABLE IF NOT EXISTS transaction_type (
        id          INTEGER,
        type        VARCHAR (10) NOT NULL
      )
      """
    )

  def transaction_function(self):
    # funcs: {'increment', 'decrement'}
    self.curr.execute(
      """
      CREATE TABLE IF NOT EXISTS transaction_function (
        id          INTEGER,
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
        id              INTEGER,
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
        id          INTEGER,
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
    """USD, CNY, JPY, RUB
    """
    self.curr.execute(
      """
      CREATE TABLE IF NOT EXISTS currency (
        id          INTEGER,
        currency    VARCHAR (10),
        value       DECIMAL (10, 2),
        created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at
      )
      """
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
        id          INTEGER,
        owner_id    INTEGER,
        balance     DECIMAL(10, 2),
        type_id     INTEGER
      )
      """
    )

  def wallet_type(self):
    # types: {'linked', 'shared', 'temporary'}
    self.curr.execute(
      """
      CREATE TABLE IF NOT EXISTS wallet_type (
        id          INTEGER,
        type        VARCHAR (10)
      )
      """
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
        id          INTEGER,
        owner_id    INTEGER,
        obj_name    VARCHAR (10),
        obj_ids     TEXT NOT NULL
      )
      """
    )

  def create_all(self):
    self.filters()


def db_create_all(DB_FILEPATH):
    with sqlite3.connect(DB_FILEPATH) as conn:
        curr = conn.cursor()

        Transaction(curr).create_all()
        TransactionTransfer(curr).create_all()
        User(curr).create_all()
        Currency(curr).create_all()
        Wallet(curr).create_all()
        Filters(curr).create_all()

        conn.commit()
