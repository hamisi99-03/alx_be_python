FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
if scale == 'C':
    converted = convert_to_fahrenheit(float(temperature))
    print(f"{temperature}°C is {converted}°F")
elif scale == 'F':
    converted = convert_to_celsius(float(temperature))
    print(f"{temperature}°F is {converted}°C")
else:
    print("invalid temperature.Please enter a numeric value")