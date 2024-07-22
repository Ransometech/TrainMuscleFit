SELECT title FROM movies
WHERE id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE name IN ('Bradley Cooper', 'Jennifer Lawrence')
        GROUP BY movie_id
        HAVING COUNT(DISTINCT person_id) = 2
    )
;
