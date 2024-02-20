from sqlalchemy import create_engine, text
import os

DB_STRING = os.environ['DB_CONN_STR']

engine = create_engine(DB_STRING)

def load_authors_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from authors"))
    authors = []
    for row in result.all():
      authors.append(row._asdict())
    return authors

def load_book_details(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM authors WHERE id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()