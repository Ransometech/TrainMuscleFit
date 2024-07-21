-- SQL query to list the names of all people who starred in Toy Story
SELECT DISTINCT name
FROM people
WHERE people.id IN
(
    SELECT person_id FROM movies
    JOIN stars ON movies.id = movie_id
    WHERE year = 2004
)
ORDER BY birth;
