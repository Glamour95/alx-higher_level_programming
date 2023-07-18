# MySQL Database Scripts

This repository contains a set of MySQL scripts that perform various tasks related to managing databases and tables. The scripts are part of the "SQL Introduction" project within the "alx-higher_level_programming" GitHub repository.

## Prerequisites

Before running these scripts, ensure you have the following:

1. MySQL Server installed on your system.
2. Access to the MySQL server with a user account that has appropriate privileges (e.g., root access).

## List of Scripts

### 0-list_databases.sql

This script lists all the databases available on your MySQL server.

Usage:

```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
1-create_database_if_missing.sql
This script creates a database named "hbtn_0c_0" if it doesn't already exist.

Usage:
$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
2-remove_database.sql
This script deletes the database "hbtn_0c_0" from your MySQL server if it exists.

Usage:
$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
3-list_tables.sql
This script lists all the tables within a specified database on your MySQL server.

Usage:
$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p <database_name>
4-first_table.sql
This script creates a table named "first_table" with two columns (id and name) in the specified database.

Usage:

$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database_name>

5-full_table.sql
This script prints the full description of the "first_table" in the specified database.

Usage:
$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p <database_name>

6-list_values.sql
This script lists all the rows in the "first_table" of the specified database.

Usage:
$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p <database_name>
7-insert_value.sql
This script inserts a new row with id=89 and name="Best School" into the "first_table" of the specified database.

Usage:
$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p <database_name>
8-count_89.sql
This script displays the number of records with id=89 in the "first_table" of the specified database.

Usage:
$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p <database_name> | tail -1

9-full_creation.sql
This script creates a table named "second_table" with three columns (id, name, and score) in the specified database. It also adds multiple rows to the "second_table."

Usage:
$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p <database_name>

10-top_score.sql
This script lists all records from the "second_table" of the specified database, ordered by score (top first).

Usage:
$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p <database_name>

11-best_score.sql
This script lists all records with a score >= 10 from the "second_table" of the specified database, ordered by score (top first).

Usage:
$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p <database_name>
12-no_cheating.sql
This script updates the score of Bob to 10 in the "second_table" without using Bob's id value, only the name field.

Usage:
$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p <database_name>
13-change_class.sql
This script removes all records with a score <= 5 from the "second_table" of the specified database.

Usage:
$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p <database_name>

14-average.sql
This script computes the score average of all records in the "second_table" of the specified database.

Usage:
$ cat 14-average.sql | mysql -hlocalhost -uroot -p <database_name>
15-groups.sql
This script lists the number of records with the same score in the "second_table" of the specified database, sorted by the number of records (descending).

Usage:
16-no_link.sql
This script lists all records of the "second_table" of the specified database, excluding rows without a name value. The results are ordered by descending score.

Usage:
$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p <database_name>

Author: Glamour95
