# importing the get_cupcakes function
from cupcakes import get_cupcakes

# Importing Flask to render a tamplate from library
from flask import Flask, render_template
app = Flask(__name__)


# Main home page @ http://localhost:8000
@app.route("/")
def home():
    return render_template("index.html", cupcakes=get_cupcakes("cupcakes.csv"))

# All cupcakes page @ http://localhost:8000/cupcakes


@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

# individual cupcakes page @ http://localhost:8000/cupcakes/cupcake_individual


@app.route("/cupcake_individual")
def individual_cupcake():
    return render_template("individual-cupcakes.html")

# Cart page @ http://localhost:8000/cupcakes/order


@app.route("/order")
def order():
    return render_template("order.html")


# Execute code when file runs as Script and application runner
if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")
