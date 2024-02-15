from flask import Flask, render_template, jsonify
from database import load_authors_from_db, load_author_details

app = Flask(__name__)

@app.route("/")
def home():
  authors = load_authors_from_db()
  return render_template('home.html', authors=authors)


@app.route("/api/authors")
def list():
  api_authors = load_authors_from_db()
  return jsonify(api_authors)

@app.route("/author/<id>")
def details(id):
  author = load_author_details(id)
  if not author:
    return "Not Found", 404
    
  return render_template('author.html', author=author)
  #return jsonify(author)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
