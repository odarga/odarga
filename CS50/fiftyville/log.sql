-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT * FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

SELECT description FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street' AND id = 295;

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

SELECT * FROM interviews WHERE year = 2023 AND month = 7 AND day = 28;

SELECT name, transcript FROM interviews WHERE year = 2023 AND month = 7 AND day = 28 AND (id = 161 OR id = 162 OR id = 163);

-- Ruth     Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--          If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- Eugene   I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
--          I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- Raymond  As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--          In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--          The thief then asked the person on the other end of the phone to purchase the flight ticket.

SELECT * FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute > 15 AND minute < 30)

SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND
(minute > 15 AND minute < 30) AND activity = 'exit';

-- plate
----------
-- 5P2BI95
-- 94KL13X
-- 6P58WS2
-- 4328GD8
-- G412CB7
-- L93JTIZ
-- 322W7JE
-- 0NTHK55

SELECT * FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street';

SELECT account_number, amount FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street'AND transaction_type = 'withdraw';

-- account_number | amount
--------------------------
-- 28500762       | 48
-- 28296815       | 20
-- 76054385       | 60
-- 49610011       | 50
-- 16153065       | 80
-- 25506511       | 20
-- 81061156       | 30
-- 26013199       | 35

SELECT * from phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;

SELECT caller, receiver from phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;

--     caller     |    receiver
----------------------------------
-- (130) 555-0289 | (996) 555-8899
-- (499) 555-9472 | (892) 555-8872
-- (367) 555-5533 | (375) 555-8161
-- (499) 555-9472 | (717) 555-1342
-- (286) 555-6063 | (676) 555-6554
-- (770) 555-1861 | (725) 555-3243
-- (031) 555-6622 | (910) 555-3251
-- (826) 555-1652 | (066) 555-9701
-- (338) 555-6650 | (704) 555-2131

SELECT * FROM airports;

-- 8  | CSF          | Fiftyville Regional Airport             | Fiftyville

SELECT * FROM flights;

SELECT destination_airport_id, hour, minute FROM flights JOIN airports ON airports.id = flights.origin_airport_id
WHERE city = 'Fiftyville' AND year = 2023 AND month = 7 AND day = 29 ORDER BY hour,minute;

-- destination_airport_id | hour | minute
--------------------------+------+-------
-- 4                      | 8    | 20
-- 1                      | 9    | 30
-- 11                     | 12   | 15
-- 9                      | 15   | 20
-- 6                      | 16   | 0

-- 4  | LGA          | LaGuardia Airport                       | New York City

SELECT * FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE origin_airport_id = 8 AND destination_airport_id = 4 AND year = 2023 AND month = 7 AND day = 29);

-- flight_id | passport_number | seat
-------------+-----------------+-----
-- 36        | 7214083635      | 2A
-- 36        | 1695452385      | 3B
-- 36        | 5773159633      | 4A
-- 36        | 1540955065      | 5C
-- 36        | 8294398571      | 6C
-- 36        | 1988161715      | 6D
-- 36        | 9878712108      | 7A
-- 36        | 8496433585      | 7B

SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND
(minute > 15 AND minute < 30) AND activity = 'exit')
INTERSECT
SELECT name FROM people WHERE passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id = 36)
INTERSECT
SELECT name FROM people WHERE phone_number IN
(SELECT caller from phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT name FROM people WHERE id IN
(SELECT person_id FROM bank_accounts JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street'AND transaction_type = 'withdraw');

-- name
---------
-- Bruce

SELECT * FROM people WHERE name = 'Bruce';
