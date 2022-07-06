# 0x0D. SQL - Introduction

## Learning Objectives
At the end of this project, we are expected to be able to explain to anyone, without the help of Google:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All SQL queries should have a comment just before (i.e. syntax above)
- All SQL keywords should be in uppercase (SELECT, WHERE…)

## More Info

### Comments for all SQL files:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
