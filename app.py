from flask import Flask, render_template, jsonify

app = Flask(__name__)

AUTHORS = [{
    'id': 1,
    'authorname': 'Charles Dickens',
    'bookname': 'David Copperfield',
    'review': 'Kino.'
}, {
    'id': 2,
    'authorname': 'Richard Bach',
    'bookname': 'Jonathan Livingston Seagull',
    'review': 'Incredible.'
}]


@app.route("/")
def home():
  return render_template('home.html', authors=AUTHORS)


@app.route("/api/authors")
def list():
  return jsonify(AUTHORS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
