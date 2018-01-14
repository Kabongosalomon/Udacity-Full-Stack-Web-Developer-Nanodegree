# Key learning points from The Backend: Databases & Applications Course

This course is a part of [Udacity's Full Stack Nanodegree program](https://www.udacity.com/nanodegree).

## Table of contents

1. Data and Tables
2. Elements of SQL
3. Python DB-API
4. Deeper Into SQL

## Data and Tables
- Databases make possible for multiple users and software to access the data without any problems.
- Databases:
  - key-value storage
  - navigational DB
  - relational databases.

- __Relational Databases__ - offer flexible tools for querying data with aggregation and join operations. Include rules for protecting consistency of our data. Data in relational database is stored in tables.
- Key in the databases must be unique.

## Elements of SQL
- SQL has many types of string types e.g char(n), varchar(n), text, ncharm  etc.
- dates have to be put in quotes.
- Here more data types can be found: https://www.postgresql.org/docs/9.4/static/datatype.html
- __Text and string types__:
  - text — a string of any length, like Python str or unicode types.
  - char(n) — a string of exactly n characters.
  - varchar(n) — a string of up to n characters.

- __Numeric types__:
  - integer — an integer value, like Python int.
  - real — a floating-point value, like Python float. Accurate up to six decimal places.
  - double precision — a higher-precision floating-point value. Accurate up to 15 decimal places.
  - decimal — an exact decimal value.

- __Date and time types__
  - date — a calendar date; including year, month, and day.
  - time — a time of day.
  - timestamp — a date and time together.
- Example of __select...where__ statement:

```
select name, birthdate from animals where species != 'gorilla' and name != 'Max';

select name from animals
where species = 'llama' and
birthdate >= '1995-01-01' and
birthdate <= '1998-12-31';
 birthdate <= '31-12-1998';
```

- comparison operators work the same in SQL like in python.

- create a table:


```python
  create table animals (  
       name text,
       species text,
       birthdate date);
```

- select clauses:
 - LIMIT 20 count OFFSET 150 - returns 20 rows but starting with 151st row
 - ORDER BY columns Desc
 GROUP BY columns - aggregates the rows that have common value
 - if you want to find out how common are names in the zoo: select name,count (* ) as num from animal group by name;

- __where__ is a restriction on the source tables.
- __having__ is a restriction on the result ...after aggregation



## Python DB-API

- This API has been defined to encourage similarity between the Python modules that are used to access databases. By doing this, we hope to achieve a consistency leading to more easily understood modules, code that is generally more portable across databases, and a broader reach of database connectivity from Python.
- It's important to always close


- __Exercise 1__:

```python
# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name asc;"
c.execute(query)
rows = c.fetchall()
# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()

```
- if we want to commit change to the database  we need to execute __commit ;__ otherwise the changes will not be executed.

```python
# This code attempts to insert a new rFow into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
#

import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()

```

- __atomicity__ - in a transaction involving two or more discrete pieces of information, either all of the pieces are committed or none are.

-  When having problems with starting up your vagrant you can try following command: __VAGRANT_PREFER_SYSTEM_BIN=1 vagrant ssh__
- PostgreSQL documentation: https://www.postgresql.org/docs/9.4/static/app-psql.html
- useful commands:
  - <em>select * from posts;</em> (shows the columns in the table)
  - <em>\d posts</em> - see the types of the columns
  - <em>\dt</em> — list all the tables in the database
  - <em>\dt+</em> — list tables plus additional information (notably, how big each table is on disk).
  - <em>\H</em> — switch between printing tables in plain text vs. HTML.
  - <em>select * from posts \watch</em> - display the contents of the posts table and refresh it every two seconds, so you can see changes to the table as you use the app.

-  SQL injection attacks - https://www.acunetix.com/websitesecurity/sql-injection/
- Bleach - is an allowed-list-based HTML sanitizing library that escapes or strips markup and attributes. Bleach can also linkify text safely, applying filters that Django’s urlize filter cannot, and optionally setting rel attributes, even on links already in the text. Bleach is intended for sanitizing text from untrusted sources. If you find yourself jumping through hoops to allow your site administrators to do lots of things, you’re probably outside the use cases. Either trust those users, or don’t.

- update is the SQL command for updating rows.
```sqlite3
update table
  set column= value
  where restriction;
```

The restriction works the same as in select and supports the same set of operators on column values. The like operator supports a simple form of text pattern-matching


## Deeper Into SQL
 - __normalization__ - it's very important idea in relational database. in a normalized database the relationships among the tables match the relationship that are really among the data.

- __Rules for normalization__:
  - every column has the same number of rows.
  - Some of more columns are key. The key provides the main type.
  - Non-key columns describe the key columns.
  - Tales should not imply relationships that don't exist.

- create table and types
```sqlite3
create table tablename (
  column1 type [constrains],
  column2 type [constrains],
    .
    .
    .
  )
```

- __References (declaring relationships)__ provide referential integrity - columns that are supposed to refer to each other are guaranteed to do so.

- __Foregin key__ is a column or set of columns in one table that uniquely identifies rows in another table.
- __Self Joins__
- __Subqueries__
  - [Scalar Subqueries](https://www.postgresql.org/docs/9.4/static/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES)
  - [Subquery Expressions](https://www.postgresql.org/docs/9.4/static/functions-subquery.html)
  - [FROM Clause](https://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-FROM)




## REFERENCES
- https://documentation.play-sql.com/display/SQL/The+Basics+of+SQL
- https://www.python.org/dev/peps/pep-0249/
- http://searchsqlserver.techtarget.com/definition/ACID
- http://bleach.readthedocs.io/en/latest/
- http://www.bkent.net/Doc/simple5.htm
- https://www.postgresql.org/docs/9.5/static/sql-select.html
- https://www.postgresql.org/docs/9.5/static/functions-string.html
- https://www.postgresql.org/docs/9.5/static/functions-aggregate.html
- [A Simple Guide to Five Normal Forms in Relational Database Theory](http://www.bkent.net/Doc/simple5.htm)