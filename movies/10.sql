-- SQL query to list the names of all people who starred in Toy Story
SELECT name FROM people
WHERE people.id IN
(
    SELECT person_id FROM directors
    JOIN ratings ON directors.movies_id = ratings.movie_id
    WHERE ratings >= 9.0
);
