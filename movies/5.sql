-- SQL query to list the titles and release years of all Harry Potter movies
SELECT title, year FROM movies
WHERE title LIKE 'Harry Potter%' ORDER BY year;
