
SELECT rating FROM ratings
WHERE movie_id IN
    (
    SELECT movies.id FROM movies
    WHERE year = 2012
    );
