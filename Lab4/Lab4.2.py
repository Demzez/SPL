class Country:
    def __init__(self, name, capital, area, population):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population

    def __str__(self):
        return self.name

countries = [
    Country('Россия', 'Москва', 17125191, 146700000),
    Country('Германия', 'Берлин', 357385, 83190556),
    Country('Китай', 'Пекин', 9596961, 1402000000)
]

def filter_by_area(countries, min_area):
    return [c for c in countries if c.area >= min_area]

def filter_by_population(countries, min_population):
    return [c for c in countries if c.population >= min_population]

print(filter_by_area(countries, 1000000))
print(filter_by_population(countries, 100000000))