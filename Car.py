class Car:

    def __init__(self, brand, color, tyresCount, doorsCount):
        self.brand = brand
        self.color = color
        self.tyresCount = tyresCount
        self.doorsCount = doorsCount

c1 = Car('Proton', 'Black', 4, 4)
c2 = Car('Produa', 'Red', 4, 4)


print(c1.brand)
print(c2.color)