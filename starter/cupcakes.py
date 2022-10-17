class Cupcake:
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


my_cupcake = Cupcake("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")

my_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

print(my_cupcake.sprinkles)
