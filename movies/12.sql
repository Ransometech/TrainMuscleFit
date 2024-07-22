SELECT title FROM movies
WHERE id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE name IN ('Bradley Cooper', 'Jennifer Lawrence')
    )
;
