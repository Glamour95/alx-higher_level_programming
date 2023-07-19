-- SQL script to list all shows without the genre Comedy from hbtn_0d_tvshows.
-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;
-- Get the show IDs that have the genre Comedy
SELECT tv_show_id FROM tv_show_genres
WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');
-- Query to list all shows without the genre Comedy
SELECT title FROM tv_shows
WHERE id NOT IN (
  SELECT tv_show_id FROM tv_show_genres
  WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
)
ORDER BY title ASC;
