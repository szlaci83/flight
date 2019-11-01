import sqlite3
import time


def create_connection(db_file='flights.db'):
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
    conn = sqlite3.connect('flights.db')
    sq = 'select last_seen ,price  from flights where dTime ="1567203600" order by last_seen'
    sql = 'SELECT price, last_seen, flight_no,dTime  FROM flights ORDER BY last_seen DESC'
    sql2 = 'SELECT MIN(price), MAX(price),MAX(price)- MIN(price), dTime from flights GROUP BY dTime'

    cur = conn.execute(sq)
    for c in cur:
        print(time.strftime('%m/%d-%A',  time.gmtime(int(c[0]))), c[1])

