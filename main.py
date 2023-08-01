import sqlite3

# creating the database and connection parameters
sql_database = sqlite3.connect('testdatabase')
cursor_layer = sql_database.cursor()

table_creation = '''create table if not exists users(
                        id integer primary key autoincrement,
                        name text not null,
                        age integer not null,
                        email text not null)'''


data_insertion = '''INSERT INTO users (name, age, email) VALUES
    ('John Doe', 25, 'john.doe@example.com'),
    ('Jane Smith', 30, 'jane.smith@example.com'),
    ('Michael Johnson', 22, 'michael.johnson@example.com'),
    ('Emily Williams', 28, 'emily.williams@example.com'),
    ('Robert Brown', 35, 'robert.brown@example.com'),
    ('Sarah Lee', 27, 'sarah.lee@example.com'),
    ('William Davis', 29, 'william.davis@example.com'),
    ('Jennifer Wilson', 31, 'jennifer.wilson@example.com'),
    ('Christopher Martinez', 26, 'christopher.martinez@example.com'),
    ('Jessica Taylor', 33, 'jessica.taylor@example.com'),
    ('Matthew Anderson', 24, 'matthew.anderson@example.com'),
    ('Amanda Thomas', 32, 'amanda.thomas@example.com'),
    ('David Rodriguez', 37, 'david.rodriguez@example.com'),
    ('Ashley Garcia', 23, 'ashley.garcia@example.com'),
    ('James Hernandez', 34, 'james.hernandez@example.com');'''


# create table to store data
sql_database.commit()

# fetching data's from the database
number_string = ','.join(str(i) for i in range(1,16))
data = cursor_layer.execute('select * from users where id in ({})'.format(number_string)).fetchall()
for row in data:
    print(f'id: {row[0]}')
    print(f'name: {row[1]}')
    print(f'age: {row[2]}')
    print(f'email: {row[3]}')
    print("=============================")