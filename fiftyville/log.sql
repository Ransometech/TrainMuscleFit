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
AND month = 7
AND day = 28
;

-- Find suspections ATM
SELECT account_number FROM atm_transactions
WHERE atm_location = 'Leggett Street'
AND year = 2023
AND month = 7
AND day = 28;

-- Check suspect bank accounts, licence, names
SELECT phone_number FROM bank_accounts
JOIN people
ON id = person_id
WHERE account_number IN
(
    SELECT account_number FROM atm_transactions
    WHERE atm_location = 'Leggett Street'
    AND year = 2023
    AND month = 7
    AND day = 28
)
AND license_plate IN
(
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute >= 15
    AND minute <= 25
    AND activity = 'exit'


);

-- Find licence plate and activity
SELECT * FROM bakery_security_logs
WHERE year = 2023
AND month = 7
AND day = 28
AND hour = 10
ORDER BY minute;
-- id 459| day 31, activity exit, license_plate 11J91FW

-- FInd call logs
SELECT * FROM phone_calls
WHERE caller IN
(
    SELECT phone_number FROM bank_accounts
    JOIN people
    ON id = person_id
    WHERE account_number IN
    (
        SELECT account_number FROM atm_transactions
        WHERE atm_location = 'Leggett Street'
        AND year = 2023
        AND month = 7
        AND day = 28
    )
    AND license_plate IN
    (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE year = 2023
        AND month = 7
        AND day = 28
        AND hour = 10
        AND minute >= 15
        AND minute <= 25
        AND activity = 'exit'

    )

)
AND year = 2023
AND month = 7
AND day = 28;

/*Retrieve the license plate number from the brakery_security_logs table based on the information provided by the witness during the interview.
Obtain the account number and bank account details through ATM transactions using the witness's information.
Link the account to individuals and select the suspect's account.
Query the call logs from the previously gathered information and identify calls with a duration of less than 60 seconds.
Select individuals associated with those calls.*/
SELECT * FROM people
WHERE phone_number IN
(
        SELECT caller FROM phone_calls
        WHERE caller IN
    (
        SELECT phone_number FROM bank_accounts
        JOIN people
        ON id = person_id
        WHERE account_number IN
        (
            SELECT account_number FROM atm_transactions
            WHERE atm_location = 'Leggett Street'
            AND year = 2023
            AND month = 7
            AND day = 28
        )
        AND license_plate IN
        (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE year = 2023
            AND month = 7
            AND day = 28
            AND hour = 10
            AND minute >= 15
            AND minute <= 25
            AND activity = 'exit'

        )

    )
    AND year = 2023
    AND month = 7
    AND day = 28
);

/*From the interviews, I found the earliest flight on the 29th.
I already gathered the suspect's phone number and now I have the passport.
I traced the flight origin and destination, identified the earliest flight, and found a single suspect.
I used the suspect's phone number to find the receiver on the day of the crime, and from the receiver's phone number, I obtained the receiver's name.*/
SELECT * FROM flights
JOIN passengers
ON id = flight_id
WHERE passport_number IN
(
    SELECT passport_number FROM people
    WHERE phone_number IN
    (
            SELECT caller FROM phone_calls
            WHERE caller IN
        (
            SELECT phone_number FROM bank_accounts
            JOIN people
            ON id = person_id
            WHERE account_number IN
            (
                SELECT account_number FROM atm_transactions
                WHERE atm_location = 'Leggett Street'
                AND year = 2023
                AND month = 7
                AND day = 28
            )
            AND license_plate IN
            (
                SELECT license_plate
                FROM bakery_security_logs
                WHERE year = 2023
                AND month = 7
                AND day = 28
                AND hour = 10
                AND minute >= 15
                AND minute <= 25
                AND activity = 'exit'

            )

        )
        AND year = 2023
        AND month = 7
        AND day = 28
        AND duration <= 60
    )


)
AND year = 2023
AND month = 7
AND day = 29;

-- suspect passport_number is 5773159633
-- Find suspect origin and destination
SELECT * FROM airports
WHERE id IN (8, 4);


-- Find the acommpliced
SELECT name FROM people
WHERE phone_number IN
(
    SELECT receiver FROM phone_calls
    WHERE caller IN
    (
        SELECT phone_number FROM people
        WHERE passport_number = 5773159633
    )
    AND year = 2023
    AND month = 7
    AND day = 28
    AND duration <= 60
);

