-- This script lists all genres in the "hbtn_0d_tvshows_rate" database by their rating.

-- Select the genre name and sum of ratings for each genre.
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
-- Left join with the "tv_show_genres" table on the "id" and "genre_id" columns.
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Left join with the "tv_shows" table on the "id" and "tv_show_id" columns.
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
-- Left join with the "tv_show_ratings" table on the "id" and "tv_show_id" columns.
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
-- Group the results by the genre name.
GROUP BY tv_genres.name
-- Sort the results in descending order by the rating_sum column.
ORDER BY rating_sum DESC;
