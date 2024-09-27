#Function to convert the temprerature
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
#Ask for temperature
    temp = float(input("Please enter the temperature value: "))

    #Ask for conversion
    print("Choose a conversion type: ")
    print("1: Celcius to Fahrenheit")
    print("2: Fahrenheit to Celcius")
    choice = int(input("Enter 1 or 2: "))

    #Perform the convesion
    if choice == 1:
       result = celcius_to_fahrenheit(temp)
       print(f"{temp}°C is equal to {result}°F")
    elif choice == 2:
       result = fahrenheit_to_celcius(temp)
       print(f"{temp}°F is equal to {result}°C")
    else:
       print("Invalid! Please enter 1 or 2")

temperature_converter()