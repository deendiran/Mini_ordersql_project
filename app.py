from flask import Flask, request, jsonify, render_template
from mini.database import Database
from mini.engine import Engine
from mini.table import Column
from mini.parser import parse


app = Flask(__name__)

db = Database()
engine = Engine(db)

@app.route("/")
def index():
    return render_template("index.html")

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


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    sql = f'INSERT INTO users VALUES ({data["id"]}, "{data["name"]}")'
    engine.execute(parse(sql))
    return jsonify({"status": "user created"})

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    sql = f'INSERT INTO orders VALUES ({data["id"]}, {data["user_id"]}, {data["product"]}, {data["amount"]})'
    engine.execute(parse(sql))
    return jsonify({"status": "order created"})

@app.route("/users", methods=["GET"])
def list_users():
    result = engine.execute({"type": "SELECT", "table": "users"})
    return jsonify(result)

@app.route("/user-orders", methods=["GET"])
def user_orders():
    sql = "SELECT * FROM users JOIN orders ON users.id = orders.user_id"
    result = engine.execute(parse(sql))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


