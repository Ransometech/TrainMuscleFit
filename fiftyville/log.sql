-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find description of crime scene reports
SELECT description FROM crime_scene_reports
WHERE year = 2023
AND month = 7
LIMIT 5;
