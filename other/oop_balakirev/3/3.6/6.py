class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight.lower(), self.price))

    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        else:
            return False
