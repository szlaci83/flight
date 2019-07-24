
SELECT * from flights where flight_no = '7854' and aTimeUTC = '1567035000';


SELECT min(price), last_seen from flights group by flight_no and aTimeUTC;