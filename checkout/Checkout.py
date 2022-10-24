class Checkout:
    class Discount:
        def __init__(self, nOfItems, price):
            self.nOfItems = nOfItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0

    def addDiscountRule(self, item, nOfItems, price):
        discount = self.Discount(nOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Item has no price")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
        self.total += self.prices[item]

    def calculateTotalPrice(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        return total

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nOfItems:
                total += self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count
        return total

    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        nOfDiscounts = count / discount.nOfItems
        total += nOfDiscounts * discount.price
        remaining = count % discount.nOfItems
        total += remaining * self.prices[item]
        return total
