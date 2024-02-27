from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import load_authors_from_db, load_book_details, add_review_to_db

app = Flask(__name__)


@app.errorhandler(403)
def forbidden(error):
  return render_template(
      'error.html',
      error_code=403,
      error_message='Forbidden, classified information'), 403


@app.errorhandler(404)
def page_not_found(error):
  return render_template(
      'error.html',
      error_code=404,
      error_message=
      'Not Found, someone typed something wrong and it was probably you.'), 404


@app.errorhandler(405)
def method_not_allowed(error):
  return render_template(
      'error.html',
      error_code=405,
      error_message='Method Not Allowed, do better sweetie.'), 405


@app.route("/")
def home():
  authors = load_authors_from_db()
  return render_template('home.html', authors=authors)


@app.route("/new")
def new():
  return render_template('new.html')


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


@app.route("/book/<id>/review", methods=['post'])
def create_review(id):
  data = request.form
  book = load_book_details(id)
  add_review_to_db(id, data)
  # return render_template('review.html', review=data, book=book)
  return redirect(url_for('review_submitted', id=id))

@app.route("/book/<id>/review/submitted")
def review_submitted(id):
    book = load_book_details(id)
    return render_template('review.html', book=book)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
