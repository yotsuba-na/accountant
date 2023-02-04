from flask import Flask, render_template

from accountant.routes import main, user
from accountant.sqldb import db_create_all


app = Flask(
  __name__,
  static_folder='static/accountant',
  template_folder='templates/accountant'
)


if __name__ == '__main__':
  with app.app_context():
    app.register_blueprint(main)
    app.register_blueprint(user)

    db_create_all(app)

  app.run(debug=True)
