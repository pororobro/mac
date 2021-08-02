class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

sonata = Car("SONATA", 2018)
g80 = Car("G80", 2019)

print(sonata.model, sonata.year)
print(g80.model, g80.year)