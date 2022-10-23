# Importing mulitple functions
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

# Importing Flask to render a tamplate, url_for, and redirect from library options
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


# Main home page @ http://localhost:8000
@app.route("/")
def home():
    cupcakes = get_cupcakes("cupcakes.csv")
    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)

# Endpoint to allow a cupcake to be added to the orders.csv


@ app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

# individual cupcakes page @ http://localhost:8000/cupcake_individual


@app.route("/individual-cupcake/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)

    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake, items_num=len(order), order_total=order_total)
    else:
        return "Sorry cupcake not found."


# Cart page @ http://localhost:8000/order


@app.route("/order")
def order():
    cupcakes = get_cupcakes("orders.csv")

    cupcakes_counted = []
    cupcake_set = set()

    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)

    for cupcake in cupcakes:
        cupcake_set.add(
            (cupcake["name"], cupcake["size"], cupcake["price"], cupcakes.count(cupcake)))

    return render_template("order.html", cupcakes=cupcake_set, items_num=len(order), order_total=order_total)


# Execute code when file runs as Script and application runner
if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")
