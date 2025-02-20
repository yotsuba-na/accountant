import pathlib


class DB:
    FILENAME: str = "db.sqlite3"
    STATIC_PATH: pathlib.Path = pathlib.Path("static")
    STATIC_PATH_ACCOUNTANT: pathlib.Path = STATIC_PATH / "accountant"
    DATABASE_FILEPATH: pathlib.Path = STATIC_PATH / FILENAME
