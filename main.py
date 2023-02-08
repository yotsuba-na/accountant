from flask import Flask, render_template

from accountant.routes import main, user
from accountant.sqldb import tables


app = Flask(
  __name__,
  static_folder='static/accountant',
  template_folder='templates/accountant'
)


# main path instead of app
if __name__ == '__main__':
  with app.app_context():
    app.register_blueprint(main)
    app.register_blueprint(user)

    tables.db_create_all(main)

  app.run(debug=True)
