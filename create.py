import sqlite3

with open("create_flights_table.sql") as sql:
    q = sql.read()
    with sqlite3.connect('flights.db') as conn:
        conn.execute(q)
        conn.commit
        conn.close
