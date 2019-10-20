import psycopg2

connection = psycopg2.connect('dbname=practicedb')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute('''
CREATE TABLE table1 (
    id INTEGER PRIMARY KEY NOT NULL,
    completed BOOLEAN NOT NULL
);
''')

SQL = 'INSERT INTO table1 VALUES (%(id)s, %(completed)s);'

data = {
    'id': 3,
    'completed': True
}

cursor.execute('INSERT INTO table1 (id, completed) VALUES (1, true);')
cursor.execute('INSERT INTO table1 VALUES (%s, %s);', (2, False))
cursor.execute(SQL, data)

cursor.execute('SELECT * FROM table1;')
res = cursor.fetchone()
print(f'res: {res}')

res2 = cursor.fetchall()
print(f'res2: {res2}')

cursor.execute('SELECT * FROM table1;')
result = cursor.fetchall()

for row in result:
    print(row)

connection.commit()

cursor.close()
connection.close()
