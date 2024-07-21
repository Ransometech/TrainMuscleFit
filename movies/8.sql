
SELECT name FROM people
WHERE people.id IN
(
    SELECT movies.id FROM movies
    WHERE title = 'Toy Story'
);
