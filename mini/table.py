# mini/table.py

class Column:
    """
    Represents a column in a table.
    """
    def __init__(self, name, col_type, primary=False, unique=False):
        self.name = name
        self.col_type = col_type  # INT or TEXT
        self.primary = primary
        self.unique = unique


class Table:
    """
    Represents a database table stored entirely in memory.
    """
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.rows = []

        # Determine primary key column (only one supported)
        self.primary_key = next(
            (c.name for c in columns if c.primary), None
        )

        # Indexes for fast lookup
        self.pk_index = {}          # primary key -> row
        self.unique_indexes = {}    # column -> {value -> row}

        for col in columns:
            if col.unique:
                self.unique_indexes[col.name] = {}
