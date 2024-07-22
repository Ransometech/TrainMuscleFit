-- SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
SELECT title FROM movies
JOIN rating ON id = movie_id
WHERE movie_id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE people.name = 'Chadwick Boseman'
    ) ORDER BY rating DESC
(
    SELECT movie_id FROM ratings
    WHERE movie_id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE people.name = 'Chadwick Boseman'
    ) ORDER BY rating DESC
)
ORDER BY rating
LIMIT 5;
