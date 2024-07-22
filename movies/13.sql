-- write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred Kevin Bacon himself should not be included
SELECT name FROM people
WHERE name != 'Kevin Bacon'
AND id IN (
    SELECT person_id
    FROM stars
    JOIN movies
    ON movie_id = id
    WHERE id IN (
        SELECT movie_id
        FROM stars
        JOIN people
        ON person_id = people.id
        WHERE name = 'Kevin Bacon'
    )
)
