# mini/database.py

from mini.table import Table

class Database:
    """
    Represents a collection of tables.
    """
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns):
        if name in self.tables:
            raise Exception(f"Table {name} already exists")

        self.tables[name] = Table(name, columns)

    def get_table(self, name):
        if name not in self.tables:
            raise Exception(f"Table {name} does not exist")
        return self.tables[name]
