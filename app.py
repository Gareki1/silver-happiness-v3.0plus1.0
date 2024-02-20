from flask import Flask, render_template, jsonify
from database import load_authors_from_db, load_book_details

app = Flask(__name__)


@app.route("/")
def home():
  authors = load_authors_from_db()
  return render_template('home.html', authors=authors)


@app.route("/about")
def about():
  return render_template('about.html', title='About')


@app.route("/api/authors")
def list():
  api_authors = load_authors_from_db()
  return jsonify(api_authors)


@app.route("/book/<id>")
def details(id):
  book = load_book_details(id)
  if not book:
    return "Not Found", 404

  return render_template('book.html', book=book)
  #return jsonify(author)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
