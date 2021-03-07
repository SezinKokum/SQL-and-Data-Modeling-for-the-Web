import psycopg2

conn = psycopg2.connect('dbname=mydb user=postgres password=secret')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS test;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE test (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cur.execute('INSERT INTO test (id, description) VALUES (1,\'Sezin\');')

cur.execute('INSERT INTO test (id, description) VALUES (2,\'Korhan\');')
# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()