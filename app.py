import requests
import sqlite3
import time

url = "https://api.skypicker.com/flights?"

TESTFROM = '25/08/2019'
TESTTO = '30/08/2019'
ADAY = 60 * 60 * 24


def create_connection(db_file='flights.db'):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print('error')
    return None


def save_flight_details(conn, flight):
    cols = ['id', 'duration', 'quality', 'flyTo', 'conversion', 'deep_link', 'airlines', 'fly_duration', 'aTimeUTC',
            'has_airport_change', 'price', 'bags_price', 'flyFrom', 'dTimeUTC', 'dTime', 'booking_token',
            'facilitated_booking_available', 'aTime', 'distance']

    route_cols = ['fare_basis', 'flight_no', 'last_seen']

    data = [str(flight[key]) for key in cols]
    data.extend([str(flight['route'][0][key]) for key in route_cols])
    conn.execute('INSERT INTO flights values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
    conn.commit()
    conn.close()


def search_flight(fly_from, fly_to, passengers, currency, date_from=None, date_to=None):
    if not date_from:
        date_from = TESTFROM
    if not date_to:
        date_to = TESTTO

    params = {'flyFrom': fly_from,
              'to': fly_to,
              'dateFrom': date_from,
              'dateTo': date_to,
              'partner': 'picky',
              'passengers': passengers,
              'curr': currency,
              'directFlights': 1,
              'locale': 'UK'}

    data = requests.get(url, params=params).json()
    return data


def save_flights(flights):
    for flight in flights:
        save_flight_details(create_connection(), flight)


if __name__ == '__main__':
    routes = [
        ['LTN', 'DEB', 1, 'GBP'],
        ('LTN', 'KSC', 1, 'GBP'),
        ('LTN', 'BUD', 1, 'GBP')
    ]
    while True:
        for route in routes:
            print("Getting:" + str(route))
            flights = search_flight(*route)['data']
            save_flights(flights)
        print('sleeping...')
        time.sleep(ADAY)
