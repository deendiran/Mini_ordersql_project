# Mini_ordersql_project

MiniSQL is a minimal, educational, in-memory relational database management system
implemented in Python. It supports a deliberately limited SQL-like syntax to
demonstrate core RDBMS concepts such as tables, indexing, constraints, joins,
and query execution.

This project was built as part of the Pesapal Junior Developer Challenge.

---

## Features

- In-memory database
- SQL-like interface
- Interactive REPL
- Table creation with typed columns
- Primary key and unique constraints
- Hash-map based indexing
- CRUD operations
- Basic INNER JOIN support
- Trivial web application demo

---

## Supported SQL Syntax

```sql
INSERT INTO users VALUES (1, "Alice");
SELECT * FROM users;
SELECT * FROM users JOIN orders ON users.id = orders.user_id;# MiniSQL – A Minimal In-Memory RDBMS with Order System Demo

MiniSQL is a small, educational, in-memory relational database management system implemented in Python.  
It supports a deliberately limited SQL-like interface to demonstrate core database concepts such as table
definition, indexing, constraints, CRUD operations, joins, and query execution.

This project was built as an entry for the **Pesapal Junior Developer Challenge**.

---

## Overview

The goal of MiniSQL is not to replicate a full SQL database, but to show clear thinking and understanding of
how relational databases work internally. The system is intentionally simple, readable, and well-documented.

The project also includes a small web application that demonstrates how the database can be used in a real
scenario through a basic **User & Order** system.

---

## Features

- In-memory relational database
- SQL-like command interface
- Interactive REPL
- Table creation with typed columns
- Primary key and unique constraints
- Hash-map based indexing
- CRUD operations (Create, Read, Update, Delete)
- Basic INNER JOIN support
- Trivial web application demonstrating database usage

---

## Supported SQL Syntax

MiniSQL supports a limited subset of SQL, including:

```sql
INSERT INTO users VALUES (1, "Bubu");
SELECT * FROM users;

INSERT INTO orders VALUES (1, 1, "Necklace", 250);
SELECT * FROM users JOIN orders ON users.id = orders.user_id;
```
The SQL grammar is intentionally strict and minimal to keep the implementation simple and understandable.

---
## Architecture

MiniSQL follows a straightforward database execution pipeline:

1. SQL string input
2. Tokenization and parsing
3. Query representation
4. Execution engine
5. In-memory data storage

Tables are stored as Python objects, rows are stored as dictionaries, and indexes are implemented using
Python dictionaries for fast lookups. JOIN operations are implemented using a nested-loop join.

---
## Web Application Demo

The project includes a small Flask web application that demonstrates a basic order system.

The web interface allows you to:

- Create users
- Create orders
- View all users
- View joined user-order data

All database operations in the web application are executed using MiniSQL — no external database is used.

---
## Running the Project
### Start the Interactive REPL

``` bash
python main.py
```

### Start the Web Application
```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

---
## Limitations

MiniSQL is intentionally limited and does not support:

- Disk persistence (data is lost on restart)
- Transactions or rollback
- Concurrency or locking
- Full SQL grammar
- Query optimization
- Multiple join types

These limitations were chosen to keep the project focused on core relational database concepts.

---
## Future Improvements
Possible future enhancements include:

- WHERE clause support
- Disk-backed storage
- Query optimization
- Foreign key constraints
- Additional join types
- Transaction support