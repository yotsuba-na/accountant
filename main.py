from flask import Flask, render_template


app = Flask(
  __name__, # static_folder='homenet/static',
)


@app.route('/')
def main():
  return render_template('homenet/finance.vue')


if __name__ == '__main__':
  app.run(debug=True)
