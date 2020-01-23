from peewee import SqliteDatabase, MySQLDatabase, PostgresqlDatabase

# Connect to SQLite
db_SQLite = SqliteDatabase('./data/employees.db')

# Connect to MySQL
mysql_db = MySQLDatabase('database', user='app', password='db_password', host='10.1.0.8', port=3306)

# Connect to a PostgreSQL database.
pg_db = PostgresqlDatabase('database', user='postgres', password='secret', host='10.1.0.9', port=5432)

# Switch db instance
db = db_SQLite

def connect():
    db.connect()

def create_tables(tables):
    db.create_tables(tables, safe=True)

def is_disconnected():
    return db.is_closed()

def disconnect():
    db.close()