SELECT name FROM people
WHERE id IN (
    SELECT movie_id
    FROM stars
    JOIN movies
    WHERE movies = 
)
