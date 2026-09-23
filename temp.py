def main():
    temp = get_temp()
    type = get_type()
    convert_temp(temp, type)

def get_temp():
    temp = float(input("Enter the temperature: "))
    return temp

def get_type():
    type = input("Please enter the temperature type (C/F/K): ")
    return type

def convert_temp(temp, type):
    if type.lower() == "c":
        temp = (temp * 9/5) + 32
        print(f"The temperature in Fahrenheit is: {temp} F")
    elif type.lower() == "f":
        temp = (temp - 32) * 5/9
        print(f"The temperature in Celsius is: {temp} C")
    elif type.lower() == "k":
        temp = temp - 273.15
        print(f"The temperature in Celsius is: {temp} C")
        temp = (temp * 9/5) + 32
        print(f"The temperature in Fahrenheit is: {temp} F")
    else:
        print("You have entered an invalid temperature type. Please enter a valid temperature type (C/F/K).")

main()