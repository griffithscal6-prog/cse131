
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def map_data(process_function, data):
    mapped_data = []
    for item in data:
        mapped_data.append(process_function(item))
    return mapped_data

import functools

def main():
    fahrenheit_temperatures = [-40, 0, 32, 100, 212]
    celsius_temperatures = map_data(fahrenheit_to_celsius, fahrenheit_temperatures)
    
    print(celsius_temperatures)

    celsius_temperatures = list(map(fahrenheit_to_celsius, fahrenheit_temperatures))
    print(celsius_temperatures)

    celsius_temperatures = list(map(lambda f: (f-32)*5/9, fahrenheit_temperatures))
    print(celsius_temperatures)

    numbers = range(1, 101)

    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(odd_numbers)

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

    total = functools.reduce(lambda n1, n2: n1 + n2, numbers)
    print(total)

    factorial = functools.reduce(lambda n1, n2: n1 * n2, numbers)
    print(factorial)

    


main()