import random
import sqlite3

connect = sqlite3.connect('my_database.db')

cursor = connect.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
    car(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    model TEXT,
    year INT,
    color TEXT,
    type TEXT)
    '''
)


model = random.choice(['audi', 'vw', 'tesla', 'mers'])
year = random.randint(2000, 2022)
color = random.choice(['yellow', 'red', 'blue', 'green'])
type = random.choice(['disel', 'gas', 'elecric'])

cursor.execute('''INSERT INTO car(model, year, color, type)
VALUES (?,?,?,?)''',(model, year, color, type))

# cursor.execute('''INSERT INTO car(model, year, color, type)
# VALUES (?,?,?,?)'''('audi', 2019, 'white', 'disel')''')
connect.commit()