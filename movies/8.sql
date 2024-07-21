
SELECT name FROM people
WHERE people.id =
(
    SELECT id FROM movies
    WHERE title = 'Toy Story'
);
