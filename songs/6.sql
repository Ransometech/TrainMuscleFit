SELECT name
FROM songs
WHERE artist_id =
(
    SELECT artists.id
    FROM artists
    WHERE artists.name = 'Post Malone'
);
