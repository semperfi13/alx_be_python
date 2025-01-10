""" # Define global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Functions for temperature conversion
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
 """

# Define global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main script for user interaction
def main():
    try:
        # Prompt the user for temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        if not temp_input.replace(".", "", 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temp_input)

        # Prompt the user for the unit of the temperature
        unit = (
            input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            .strip()
            .upper()
        )

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError(
                "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."
            )

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
