from flask import Flask, render_template


app = Flask(
  __name__,
  static_folder='static/accountant',
  template_folder='templates/accountant'
)


@app.route('/')
def main():
  return render_template('main.vue')


if __name__ == '__main__':
  app.run(debug=True)
