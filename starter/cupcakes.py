# Imports the abstract method into the file
from abc import ABC, abstractmethod

# Imports pretty prin into the file, allowing the csv files to be formatted in the terminal
from pprint import pprint

# Importing the csv fies for the realted funcitons to run
import csv

# Parent Class with an Abstract requiring calculate_price function


class Cupcake(ABC):
    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

# Child Class for a Regular cupcake with required abstract from parent class


class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price


# Child Class defining initiates and fields for a mini cupcake with required abstract from parent class


class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price


# Child Class for a Large cupcake with required abstract from parent class
class Large(Cupcake):
    size = "large"

    def calculate_price(self, quantity):
        return quantity * self.price


# Cupcake instances
cupcake1 = Regular("Apple Pie", 3.39,
                   "cinnamon-apple", "cinnamon buttercream", "fresh apple filling")
cupcake1.add_sprinkles("Red", "White", "Chocolate")
cupcake2 = Mini("Country Cherry Cheesecake", 2.39,
                "graham cracker", "vanilla buttercream")
cupcake2.add_sprinkles("country cherry filling")
cupcake3 = Large("Lemon Drop", 5.39, "lemon cake",
                 "lemon buttercream", "fresh lemon curd")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]


# Function to append the sample.csv file and add new instances to the list


def add_cupcake(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor",
                      "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor,
                                "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price,
                                "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


# add_cupcake("sample.csv", cupcake_list)
# Un-note the above line to write an entirely new list to the sample.csv file


# Function to write over the sample.csv file and create a new list based on the instances above


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor",
                      "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor,
                                "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price,
                                "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


# write_new_csv("sample.csv", cupcake_list)
# Un-note the above line to write an entirely new list to the sample.csv file


# Function to add the cupcake dictionaries to file
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

# Function to read the csv files


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# read_csv("sample.csv")
# Un-note the above line to read csv files to the terminal
