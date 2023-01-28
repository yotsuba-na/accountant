from flask import Flask, render_template


app = Flask(
  __name__,
  static_folder='static/homenet',
  template_folder='templates/homenet'
)


@app.route('/')
def main():
  return render_template('finance.vue')


if __name__ == '__main__':
  app.run(debug=True)
