SELECT COUNT(*) FROM movies
JOIN ratings ON movies.id = movie_id
WHERE rating = 10;
