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
