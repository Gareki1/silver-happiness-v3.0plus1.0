from sqlalchemy import create_engine, text
import os

DB_STRING = os.environ['DB_CONN_STR']

engine = create_engine(DB_STRING)

def load_authors_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select authorname, bookname, review from authors"))
    authors = []
    for row in result.all():
      authors.append(row._asdict())
    return authors