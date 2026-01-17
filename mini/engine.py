# mini/engine.py

class Engine:
    """
    Executes parsed SQL commands against the database.
    """
    def __init__(self, database):
        self.db = database

    def execute(self, query):
        if query["type"] == "INSERT":
            return self._insert(query)

        if query["type"] == "SELECT":
            return self._select(query)
        
        if query["type"] == "JOIN":
            return self._join(query)


    def _insert(self, query):
        table = self.db.get_table(query["table"])
        values = query["values"]

        row = {}
        for col, val in zip(table.columns, values):
            clean = val.strip().strip("(").strip(")").strip('"')
            row[col.name] = clean


        # Enforce primary key constraint
        if table.primary_key:
            pk = row[table.primary_key]
            if pk in table.pk_index:
                raise Exception("Duplicate primary key")

            table.pk_index[pk] = row

        # Enforce unique constraints
        for col_name, index in table.unique_indexes.items():
            val = row[col_name]
            if val in index:
                raise Exception(f"Duplicate value for unique column {col_name}")
            index[val] = row

        table.rows.append(row)
        return "1 row inserted"

    def _select(self, query):
        table = self.db.get_table(query["table"])
        return table.rows
    
    def _join(self, query):
        left = self.db.get_table(query["left"])
        right = self.db.get_table(query["right"])

        results = []

        for lrow in left.rows:
            for rrow in right.rows:
                if lrow[query["left_col"]] == rrow[query["right_col"]]:
                    combined = {}
                    combined.update({f"{left.name}.{k}": v for k, v in lrow.items()})
                    combined.update({f"{right.name}.{k}": v for k, v in rrow.items()})
                    results.append(combined)

        return results

