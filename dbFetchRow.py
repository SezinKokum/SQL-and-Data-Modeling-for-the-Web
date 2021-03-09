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
  CREATE TABLE test3 (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cur.execute('INSERT INTO test3 (id, description) VALUES (%s, %s);',(1,'Sezin'))
# commit, so it does the executions on the db and persists in the db

SQL = 'INSERT INTO test3 (id, description) VALUES (%(id)s, %(description)s);'

data = {
  'id': 2,
  'description': 'Korhan'
}
cursor.execute(SQL, data)

cur.execute('INSERT INTO test3 (id, description) VALUES (%s, %s);',(3,'Nur'))
cur.execute('INSERT INTO test3 (id, description) VALUES (%s, %s);',(4,'Goksel'))

cursor.execute('SELECT * from test3;')
result = cursor.fetchmany(2) #first two element is now, [(1, 'Sezin'), (2, 'Korhan')]
print('fetchmany(2)',result)

result2 = cursor.fetchone() #the element where the cursor is now, (3, 'Nur')
print('fetchone',result2)

result3 = cursor.fetchall() #the element where the cursor is now, [(4, 'Goksel')]. If it was the first command for example if it was in line 35, it would print the result all elements.
print('fetchall',result3)

conn.commit()

cur.close()
conn.close()