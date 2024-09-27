#Function to calculate voltage
def calculate_voltage(current, resistance):
    return current * resistance

#Function to calculate current
def calculate_current(voltage, resistance):
    if resistance == 0:
        return "Error: Resistance cannot be zero. Input the right value."
    return voltage / resistance

#Function to calculate resistance
def calculate_resistance(voltage, current):
    if current == 0:
        return "Error: Current cannot be zero. Input the right value."
    return voltage / current

#Using Ohm's Law
def ohms_law_calculator():
    print("What would you like to calculate?")
    print("1: Voltage")
    print("2: Current")
    print("3: Resistance")
    choice = int(input("Enter 1, 2, or 3: "))

    if choice == 1:
        #Calculate Voltage
        current = float(input("Enter the current in ampere: "))
        resistance = float(input("Enter the resistance in ohms: "))
        voltage = calculate_voltage(current, resistance)
        print(f"The voltage is {voltage} volts.")
    
    elif choice == 2:
        #Calculate Current
        voltage = float(input("Enter the voltage in volts: "))
        resistance = float(input("Enter the resistance in ohms: "))
        current = calculate_current(voltage, resistance)
        print(f"The current is {current} amperes.")

    elif choice == 3:
        #Calculate Resistance
        voltage = float(input("Enter the voltage in volts: "))
        current = float(input("Enter the current in ampere: "))
        resistance = calculate_resistance(voltage, current)
        print(f"The resistance is {resistance} ohms.")
    
    else:
        print("Invalid selection. Please enter 1, 2, or 3.")

ohms_law_calculator()