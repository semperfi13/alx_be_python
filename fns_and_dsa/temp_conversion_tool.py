FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


celcius = 0
fahrenheit = 0

temperature = int(input("Enter the temperature to convert: "))

type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if type == "c":
    celcius += temperature
    result = convert_to_fahrenheit(celcius)
    print(f"{celcius}°F is {result}°C")
elif type == "f":
    fahrenheit += temperature
    result = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {result}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
