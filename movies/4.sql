-- SQL query to determine the number of movies with an IMDb rating of 10.0
SELECT COUNT(*) FROM movies
JOIN ratings ON movies.id = movie_id
WHERE rating = 10;
