cars = ["saab", "volvo", "volkswagen", "bmw", "nissan", "renault", "kia", "toyota", "ford", "fiat"]

sorted(cars)
print(cars)
print(sorted(cars))

cars.sort()
print(cars)

print(sorted(cars, reverse=True))

cars.sort(reverse=True)
print(cars)

car_models = [
    ("saab","9-3"),
    ("volvo","740"),
    ("volkswagen","passat"),
    ("bmw","323"),
    ("nissan","almera"),
    ("renault","clio"),
    ("kia","ceed"),
    ("toyota","corolla"),
    ("ford","focus"),
    ("fiat","500")
]


print(sorted(car_models, key=lambda k: k[0]))
print(sorted(car_models, key=lambda k: k[1]))