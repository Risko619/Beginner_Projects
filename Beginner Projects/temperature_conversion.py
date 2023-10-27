# Ask the user which conversion they want to perform
conversion_choice = input("Choose conversion (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): ")

if conversion_choice == '1':
    # Conversion from Celsius to Fahrenheit
    celsius_temperature = float(input("Enter temperature in Celsius: "))
    # Calculate Fahrenheit
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")
elif conversion_choice == '2':
    # Conversion from Fahrenheit to Celsius
    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    # Calculate Celsius
    celsius_temperature = (fahrenheit_temperature - 32) * 5/9
    print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature} degrees Celsius.")
else:
    print("Invalid choice. Please enter 1 or 2 for the conversion.")
