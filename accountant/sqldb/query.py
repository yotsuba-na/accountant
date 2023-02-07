def list_to_query_str(target: list) -> str:
  if len(target) == 1:
    return f"({target[0]})"
  return str(tuple(target))


class User:
  """Query for `user` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_all(self, by_ids: list[int] | None) -> list:
    query = 'SELECT * FROM user'

    if by_ids is not None:
      query += f" WHERE id IN {list_to_query_str(by_ids)}"

    return self.curr.execute(query).fetchall()


class Filters:
  """Query for `filters` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_user_filter(self, user_id: int, obj_name: str) -> list:
    """Gets user filter for `obj_name` table
    """
    obj_ids = self.execute(
      f"""
      SELECT obj_ids FROM filters WHERE uid={user_id} AND obj_name={obj_name}
      """
    ).fetchone()

    if obj_ids is not None:
      obj_ids = list(map(int, objids.split(',')))

    return obj_ids


class Schedules:
  """Query for `schedules` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_users_schedules(self, users_id: list[int] | None):
    """Users schedules
    """
    query = "SELECT * FROM schedule"

    if users_id is not None:
      query += f" WHERE u_id IN {list_to_query_str(users_id)}"

    return self.curr.execute(query).fetchall()


class Todo:
  """Query for `todo` table
  """
  def __init__(self, curr):
    self.curr = curr

  def get_users_todo(self, users_id: list[int] | None):
    """Users todo
    """
    query = "SELECT * FROM todo"

    if users_id is not None:
      query += f" WHERE u_id IN {list_to_query_str(users_id)}"

    return self.curr.execute(query).fetchall()
