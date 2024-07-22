-- SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
SELECT title,rating FROM movies
JOIN ratings ON id = movie_id
WHERE movie_id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE people.name = 'Chadwick Boseman'
    )

ORDER BY rating DESC
LIMIT 5;
