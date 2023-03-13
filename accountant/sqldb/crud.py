def list_to_query_str(target: list) -> str:
  if len(target) == 1:
    return f"({target[0]})"
  return str(tuple(target))


class User:
  """Query for `user` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_all(self, by_ids: list[int] | None = None) -> list:
    query = 'SELECT * FROM user'

    if by_ids is not None:
      query += f" WHERE id IN {list_to_query_str(by_ids)}"

    return self.curr.execute(query).fetchall()


class Filter:
  """Query for `filters` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get(self, user_id: int, obj_name: str) -> list:
    """Gets user filter for `obj_name` table
    """
    obj_ids = self.curr.execute(
      f"""
      SELECT obj_ids FROM filters
      WHERE owner_id={user_id} AND obj_name='{obj_name}'
      """
    ).fetchone()

    if obj_ids is not None:
      obj_ids = list(map(int, obj_ids.split(',')))

    return obj_ids


class Transaction:
  """Query for `transaction` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_all(self, users_id: list[int] | None = None):
    """Users schedules
    """
    query = "SELECT * FROM `transaction`"

    if users_id is not None:
      query += f" WHERE owner_id IN {list_to_query_str(users_id)}"

    return self.curr.execute(query).fetchall()


class Currency:
  """Query for `currency` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_all(self, by_ids: list[int] | None = None) -> list:
    query = 'SELECT * FROM currency'

    if by_ids is not None:
      query += f" WHERE id IN {list_to_query_str(by_ids)}"

    return self.curr.execute(query).fetchall()


class Wallet:
  """Query for `wallet` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_all(self, by_ids: list[int] | None = None) -> list:
    query = 'SELECT * FROM wallet'

    if by_ids is not None:
      query += f" WHERE id IN {list_to_query_str(by_ids)}"

    return self.curr.execute(query).fetchall()
