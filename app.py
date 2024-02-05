from flask import Flask, render_template, jsonify

app = Flask(__name__)

AUTHORS = [{
    'id':
    1,
    'name':
    'Charles Dickens',
    'nationality':
    'British',
    'famouswork': ['David Copperfield', 'Oliver Twist', 'Pickwick Papers']
}, {
    'id': 2,
    'name': 'Leo Tolstoy',
    'nationality': 'Russian',
    'famouswork': 'War and Peace'
}, {
    'id': 3,
    'name': 'Mark Twain',
    'nationality': 'AmeriKKKan',
    'famouswork': 'The Adventures of Tom Sawyer'
}, {
    'id': 4,
    'name': 'RK Narayan',
    'nationality': 'Indian',
    'famouswork': 'Malgudi Days'
}, {
    'id':
    5,
    'name':
    'Oscar Wilde',
    'nationality':
    'Irish',
    'famouswork':
    ['The Importance of Being Earnest', 'The Picture of Dorian Gray']
}, {
    'id': 6,
    'name': 'Nagaru Tanigawa',
    'nationality': 'Japanese',
    'famouswork': 'The Melancholy of Haruhi Suzumiya'
}]


@app.route("/")
def home():
  return render_template('home.html', authors=AUTHORS)

@app.route("/api/authors")
def list():
  return jsonify(AUTHORS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
