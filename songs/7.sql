SELECT AVG(energy)
FROM songs
WHERE artist_id =
(
    SELECT artists.id
    FROM artists
    WHERE artists.name = 'Drake'
);
