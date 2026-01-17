# minisql/repl.py

from mini.parser import parse
from mini.engine import Engine

def start_repl(engine):
    print("Welcome to MiniSQL. Type 'exit' to quit.")

    while True:
        sql = input("MiniSQL> ")

        if sql.lower() in ("exit", "quit"):
            break

        try:
            query = parse(sql)
            result = engine.execute(query)
            print(result)
        except Exception as e:
            print("Error:", e)
