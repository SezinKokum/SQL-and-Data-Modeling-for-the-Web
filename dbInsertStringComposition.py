import psycopg2

conn = psycopg2.connect('dbname=mydb user=postgres password=secret')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS test2;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE test2 (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cur.execute('INSERT INTO test2 (id, description) VALUES (%s, %s);',(1,'Sezin'))
# commit, so it does the executions on the db and persists in the db

SQL = 'INSERT INTO test2 (id, description) VALUES (%(id)s, %(description)s);'

data = {
  'id': 2,
  'description': 'Korhan'
}
cursor.execute(SQL, data)
conn.commit()

cur.close()
conn.close()