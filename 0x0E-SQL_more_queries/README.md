SQL Queries

This repository contains SQL scripts to perform various queries on a MySQL database called hbtn_0d_tvshows. Below is a brief description of each script along with instructions on how to use them.

Prerequisites
You need to have MySQL installed on your local machine or server.
The database hbtn_0d_tvshows must be imported into your MySQL server. You can use the provided dump file for this purpose.

1. 10-genre_id_by_show.sql
This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

Usage:
$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

2. 11-genre_id_all_shows.sql
This script lists all shows contained in the hbtn_0d_tvshows database.

Usage:

$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

3. 12-no_genre.sql
This script lists all shows contained in hbtn_0d_tvshows without a genre linked.

Usage:

$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

4. 13-count_shows_by_genre.sql
This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each genre.

Usage:

$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

5. 14-my_genres.sql
This script lists all genres of the show "Dexter" in the hbtn_0d_tvshows database.

Usage:

$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

6. 15-comedy_only.sql
This script lists all Comedy shows in the hbtn_0d_tvshows database.

Usage:

$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

7. 16-shows_by_genre.sql
This script lists all shows and all genres linked to each show from the hbtn_0d_tvshows database.

Usage:

$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows



