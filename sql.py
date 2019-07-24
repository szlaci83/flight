import sqlite3


def create_connection(db_file='C:\Users\Laszlo.Szoboszlai\personal\git\\flight\\flights.db'):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print('error')
    return None


def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        return c
    except:
        print('error')


def execute_sql_file(filename):
    with open(filename, 'r') as f:
        sql = f.read()
        execute_sql(create_connection(), sql)


if __name__ == '__main__':
    #execute_sql_file('create_flights_table.sql')
    conn = sqlite3.connect('C:\Users\Laszlo.Szoboszlai\personal\git\\flight\\flights.db')
    cur = conn.execute('SELECT * FROM flights')
    i = 0
    for c in cur:
        print(i)
        print(c)
        i += 1