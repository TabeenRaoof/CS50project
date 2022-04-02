-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = "Humphrey Street"; -- to find the report on the stopen duck



SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 and day = 28 AND transcript LIKE "%bakery%"; -- brings up the transcript of the interviews that are relevant (i.e. same day and mentions bakery)

--Transcript 1
--| Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |


-- from first transcirpt, the theif left the parking between 10:15am and 10:25am
SELECT name FROM people
    OIN bakery_security_logs ON bakery_security_logs.license_plate = people.License_plate
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <+ 25
    AND activity = "exit"; -- this will join "bakery_security_logs" and "people" tables to find the suspects through the timings from above

-- from the above, we have the names of 8 suspects:
--+---------+
--|  name   |
--+---------+
--| Vanessa |
--| Bruce   |
--| Barry   |
--| Luca    |
--| Sofia   |
--| Iman    |
--| Diana   |
--| Kelsey  |
--+---------+

--Transcript 2
--| I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
SELECT name FROM people
    JOIN bank_accounts ON bank_accounts.person_id = people.id
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"; -- "bakery_security_logs" and "people" with atm_transactions tables to find suspects based on the street name in above transctipt

-- from the above, we have the names of 8 suspects:
-----------+
--|  name   |
--+---------+
--| Bruce   |--
--| Diana   |--
--| Brooke  |
--| Kenny   |
--| Iman    |--
--| Luca    |--
--| Taylor  |
--| Benista |
--+---------+


--Transcript 3
--| As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- JOIN TABLES airports - flights - passengers - people

SELECT name FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    WHERE passengers.flight_id = (SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
    SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour, minute LIMIT 1); -- joins 4 tables airports - flights - passengers - people to find the name of suspects based on the earliest flight tomorrow

-- based on above, we have 8 suspects:
--+--------+
--|  name  |
--+--------+
--| Doris  |
--| Sofia  |
--| Bruce  |--
--| Edward |
--| Kelsey |
--| Taylor |
--| Kenny  |
--| Luca   |--
--+--------+


--Transcript 4
--| I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour. They never bought anything.

SELECT name FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration <= 60;


-- from above, we have 10 suspects:
--+---------+
--|  name   |
--+---------+
--| Sofia   |
--| Kelsey  |
--| Bruce   |-- commen suspect
--| Kathryn |
--| Kelsey  |
--| Taylor  |
--| Diana   |
--| Carina  |
--| Kenny   |
--| Benista |
--+---------+

-- the only common suspect among all 4 queries is Bruce.
-- Conclusion: Bruce is the theif.


--find destination city
SELECT city FROM airports
    JOIN flights ON flights.destination_airport_id = airports.id
    WHERE flights.id = (SELECT flight_id from passengers WHERE year = 2021 AND month = 7 AND day = 29 AND passport_number = (
    SELECT passport_number FROM people WHERE name = "Bruce")); -- joins 3 tables airports, flights and people to find the name of the destination city of Bruce

--+---------------+
--|     city      |
--+---------------+
--| New York City |
--+---------------+



-- find accomplice
SELECT name FROM people
    WHERE phone_number = (SELECT receiver FROM phone_calls
    WHERE day = 28 AND month = 7 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE name = "Bruce")); -- finds the name of the accomplice by matching the phone number that Bruce called

--+-------+
--| name  |
--+-------+
--| Robin |
--+-------+