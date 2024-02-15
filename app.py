from flask import Flask, render_template, jsonify
from database import load_authors_from_db

app = Flask(__name__)

# AUTHORS = [{
#     'id': 1,
#     'authorname': 'Charles Dickens',
#     'bookname': 'David Copperfield',
#     'review': 'Kino.'
# }, {
#     'id': 2,
#     'authorname': 'Richard Bach',
#     'bookname': 'Jonathan Livingston Seagull',
#     'review': 'Incredible.'
# }]


@app.route("/")
def home():
  authors = load_authors_from_db()
  return render_template('home.html', authors=authors)


@app.route("/api/authors")
def list():
  api_authors = load_authors_from_db()
  return jsonify(api_authors)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
