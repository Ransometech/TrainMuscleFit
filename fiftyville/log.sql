-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find description of crime scene reports
SELECT * FROM crime_scene_reports
WHERE year = 2023
AND month = 7
AND street = 'Humphrey Street';
/* id 295. Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time
 – each of their interview transcripts mentions the bakery.*/

-- Use interviews to find suspects
SELECT * FROM interviews
WHERE year = 2023
AND month = 8
LIMIT 1;

-- Find suspections ATM
SELECT * FROM atm_transactions
WHERE atm_location = 'Humphrey Lane'
AND year = 2023
AND month = 7
AND day = 28
LIMIT 5;


-- Find licence plate and activity
SELECT * FROM bakery_security_logs
WHERE year = 2023
AND month = 7
AND minute = 15
AND hour = 10;
-- id 459| day 31, activity exit, license_plate 11J91FW

-- FInd suspect with LICENSE Plate
SELECT * FROM people
WHERE license_plate = '11J91FW';


