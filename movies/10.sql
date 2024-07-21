-- SQL query to list the names of all people who starred in Toy Story
SELECT DISTINCT name FROM people
WHERE people.id IN
(
    SELECT person_id FROM directors
    JOIN ratings ON directors.movie_id = ratings.movie_id
    WHERE rating >= 9.0
)
ORDER BY birth;
