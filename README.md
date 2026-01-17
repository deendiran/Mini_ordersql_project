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
SELECT * FROM users JOIN orders ON users.id = orders.user_id;
