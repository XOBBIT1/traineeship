import random

cars_models = [
    "Aston Martin",
    "Audi",
    "Bentley",
    "BMW",
    "Cadillac",
    "Chevrolet",
    "Citroen",
    "Ferrari",
    "Ford",
    "Honda",
    "Hyundai",
    "Kia",
    "LADA",
    "Lamborghini",
    ]


colors = ['Red', 'White', 'Blue', "Black", 'Green', 'Grey', 'Purple', 'Yellow']
body_types = ['Hatchback', 'Minivan', 'CrossOverVehicle', 'Coupe', 'Supercar', 'Cabriolet', 'Sedan', 'Micro']
name_list = ["LOXA", 'Ichigo', 'Luffy', 'Naruto', 'Goku', 'Madara', 'Izen', 'Jozef Jostar', 'Dio', 'Satoru']
description = ["Car for salon!!!", "Car for BOND!!!", "My Car)!"]
description_provider = ["The best provider", "A man which you ca believe", "Dangen Master!"]
location = ["BR", "UK", "US", "AF"]
salon_name = ["LOXAS_SALON", 'Ichigos_salon', 'Luffys_salon', 'Narutos_salon', 'Gokus_salon', 'Madaras_salon']


def random_salon_name():
    return random.choice(salon_name)


def random_location():
    return random.choice(location)


def random_description_provider():
    return random.choice(description_provider)


def random_description():
    return random.choice(description)


def random_cars_models():
    return random.choice(cars_models)


def random_color():
    return random.choice(colors)


def random_body_types():
    return random.choice(body_types)


def random_name():
    return random.choice(name_list)


def random_year():
    return random.randint(1981, 2022)
