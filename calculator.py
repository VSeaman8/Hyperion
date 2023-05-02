# Program to calculate user entered numbers and operator, add to a txt document and then print out the document

# Define the function to perform addition
def add(num1, num2):
    return num1 + num2

# Define the function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Define the function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Define the function to perform division and value error for 2nd number being 0 with divide
def divide(num1, num2):
    try:
        if num2 == 0:
            raise ValueError ("Cannot divide by zero. Please enter a new 2nd number:")
        return num1 / num2
    except ValueError as e:
        print(e)
        while True:
            try:
                num2 = float(input("Please enter a new number: "))
                break
            except ValueError:
                print("Invalid input. Please reenter a number.")
        return divide(num1, num2)
    
# open my_calculations txt file
while True:
    try: 
        file = open("your_calculations.txt", "w")
        break
    except FileNotFoundError:
        print("oh dear!, Looks like your txt file has gotten lost. Please try again")

# User input
while True:
    # ask the user to input the first number
    while True:
        try:
            num1 = float(input("Please enter the first number: "))
            break
        except ValueError:
            print("Ooops! not valid please enter a number")
            
    # ask the user to input the operator
    while True:
        try:
            operator = input("Please enter the operator (+, -, *, /): ")
            break
    
        except ValueError:
            print("Ooops! not valid please enter a number")
            
    # ask the user to input the second number
    while True:
        try:
            num2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Ooops! not valid please enter a number")
            
    # perform the calculation based on the operator entered
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
   
    # print the result
    print(f"{num1} {operator} {num2} = {round(result, 2)}")

    # write the calculation to file 
    file.write(f"{num1} {operator} {num2} = {round(result, 2)}"+ "\n")

    # asks user if they would like to enter another calculation
    start_loop = input("Would you like to do another calculation (y/n)?") 

    # if user enters y then loop starts again   
    if start_loop.lower().strip() == "y": 
        continue
    # if user enters n then loop breaks, saves calculations to txt file and then prints
    else:
        file.close()
        print(f"results saved to your_calculations.txt")
        file = open("your_calculations.txt", "r")
        lines = file.readlines()

        for line in lines:
            temp = line.strip()
            temp = temp.split(" = ")
            print(temp[0])
        file.close()
        break

