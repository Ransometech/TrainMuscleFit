SELECT name FROM people
WHERE name != 'Kevin Bacon'
AND WHERE id IN (
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
