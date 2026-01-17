def parse(sql):
    tokens = sql.strip().replace(",", "").split()
    command = tokens[0].upper()

    if command == "INSERT":
        return {
            "type": "INSERT",
            "table": tokens[2],
            "values": tokens[4:]
        }

    if command == "SELECT" and "JOIN" in tokens:
        return {
            "type": "JOIN",
            "left": tokens[3],      # users
            "right": tokens[5],     # orders
            "left_col": tokens[7].split(".")[1],     # id          
            "right_col": tokens[9].split(".")[1]     # user_id
        }

    raise Exception("Unsupported SQL command")
