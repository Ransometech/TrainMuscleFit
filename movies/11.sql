SELECT title FROM movies
WHERE id IN
(
    SELECT movie_id FROM ratings
    WHERE movie_id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE people.name = 'Chadwick Boseman'
    ) ORDER BY rating
)
;
