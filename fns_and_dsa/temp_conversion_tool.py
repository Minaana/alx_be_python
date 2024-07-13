FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature value: "))
        unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == 'F':
            celsius_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equivalent to {celsius_temp:.2f}°C.")
        elif unit == 'C':
            fahrenheit_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equivalent to {fahrenheit_temp:.2f}°F.")
        else:
            print("Invalid temperature unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()