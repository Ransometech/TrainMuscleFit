SELECT title, rating FROM movies
JOIN ratings ON id = movie_id
WHERE year = 2010 ORDER BY rating, title LIMIT 50;
