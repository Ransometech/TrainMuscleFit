SELECT title FROM movies
WHERE id IN
(
    SELECT person_id FROM directors
    JOIN ratings ON directors.movie_id = ratings.movie_id
    WHERE rating >= 9.0
)
ORDER BY birth;
