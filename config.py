import os


class DB:
  FILENAME = 'db.sqlite3'
  FILEPATH = os.path.join('static', 'accountant')
  if not os.path.exists(FILEPATH):
    os.makedirs(FILEPATH, exist_ok=True)
  FILEPATH = os.path.join(FILEPATH, FILENAME)
