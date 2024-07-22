SELECT title, FROM movies
WHERE movie_id IN (
        SELECT movie_id FROM stars
        JOIN people ON person_id = people.id
        WHERE people.name = 'Chadwick Boseman'
    )

ORDER BY rating DESC
LIMIT 5;
