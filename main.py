# main.py

from mini.database import Database
from mini.engine import Engine
from mini.repl import start_repl
from mini.table import Column

db = Database()

# Create tables
db.create_table("users", [
    Column("id", "INT", primary=True),
    Column("name", "TEXT")
])

db.create_table("orders", [
    Column("id", "INT", primary=True),
    Column("user_id", "INT"),
    Column("product", "TEXT"),
    Column("amount", "INT")
])

engine = Engine(db)
start_repl(engine)
