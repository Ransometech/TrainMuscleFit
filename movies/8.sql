
SELECT name FROM people
WHERE people.id IN
(
    SELECT movies.id FROM movies
    JOIN 
    WHERE title = 'Toy Story'
);
