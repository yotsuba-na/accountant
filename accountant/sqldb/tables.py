import sqlite3
from os.path import join
import os

from flask import url_for


class Currency:
  def __init__(self, conn):
    self.conn = conn

  def currency(self):
    """USD, CNY, JPY, RUB
    """
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS currency (
        id INTEGER,
        currency VARCHAR(10),
        value DECIMAL(10, 2),
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
      """
    )

  def create_all(self):
    self.currency()

    self.conn.commit()


class User:
  def __init__(self, conn):
    self.conn = conn

  def user(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS user (
        id INTEGER,
        nickname VARCHAR(50),
        currency_id INTEGER
      )
      """
    )

  def create_all(self):
    self.user()

    self.conn.commit()


class Wallet:
  def __init__(self, conn):
    self.conn = conn

  def wallet(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS wallet (
        id INTEGER,
        uid SMALLINT,
        balance DECIMAL(10, 2),
        shared BOOLEAN
      )
      """
    )

  def create_all(self):
    self.wallet()

    self.conn.commit()


class Scheduled:
  def __init__(self, conn):
    self.conn = conn

  def schedule_code(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS schedule_code (
        id INTEGER,
        uid SMALLINT,
        code VARCHAR(10)
      )
      """
    )

  def func_code(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS func_code (
        id INTEGER,
        uid SMALLINT,
        code VARCHAR(10)
      )
      """
    )

  def schedule(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER,
        uid SMALLINT,
        title VARCHAR(50),
        schedule_code_id SMALLINT,
        func_code_id SMALLINT,
        value DECIDMAL(10, 2),
        wid SMALLINT
      )
      """
    )

  def create_all(self):
    self.schedule_code()
    self.func_code()
    self.schedule()

    self.conn.commit()


class Filters:
  def __init__(self, conn):
    self.conn = conn

  def filters(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS filters (
        id INTEGER,
        uid SMALLINT,
        obj_name VARCHAR(30),
        obj_ids VARCHAR(50)
      )
      """
    )

  def create_all(self):
    self.filters()

    self.conn.commit()


class Todo:
  def __init__(self, conn):
    self.conn = conn

  def todo_currency(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS todo_currency (
        id INTEGER,
        tid SMALLINT,
        currency_id SMALLINT,
        value DECIMAL(10, 2)
      )
      """
    )

  def todo(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS todo (
        id INTEGER,
        uid SMALLINT,
        title VARCHAR(50),
        state BOOLEAN,
        todo_currency_id INTEGER,
        value DECIMAL(10, 2),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
      """
    )

  def todo_item(self):
    self.conn.execute(
      """
      CREATE TABLE IF NOT EXISTS todo_item (
        id INTEGER,
        uid SMALLINT,
        tid SMALLINT,
        title VARCHAR(50),
        state BOOLEAN,
        todo_currency_id INTEGER,
        value DECIMAL(10, 2),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
      """
    )

  def create_all(self):
    self.todo_currency()
    self.todo()
    self.todo_item()

    self.conn.commit()


def get_db_path(app):
    file = 'db.sqlite3'
    path = join(app.root_path, 'static', 'accountant')
    os.makedirs(path, exist_ok=True)

    return join(path, file)


def db_create_all(app):
  with sqlite3.connect(get_db_path(app)) as conn:
    Currency(conn).create_all()
    User(conn).create_all()
    Wallet(conn).create_all()
    Scheduled(conn).create_all()
    Filters(conn).create_all()
    Todo(conn).create_all()
