SELECT name FROM people
WHERE id IN (
    SELECT person_id
    FROM stars
    JOIN movies
    ON movie_id = id
    WHERE movies =
)
