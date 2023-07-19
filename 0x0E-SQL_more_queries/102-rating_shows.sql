-- This script lists all shows from the "hbtn_0d_tvshows_rate" database by their rating.

-- Select the show title and sum of ratings for each show.
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
-- Left join with the "tv_show_ratings" table on the "id" and "tv_show_id" columns.
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
-- Group the results by the show title.
GROUP BY tv_shows.title
-- Sort the results in descending order by the rating_sum column.
ORDER BY rating_sum DESC;
