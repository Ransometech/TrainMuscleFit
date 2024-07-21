
SELECT name FROM people
WHERE people.id IN
(
    SELECT person_id FROM movies
    JOIN stars
    WHERE title = 'Toy Story'
);
