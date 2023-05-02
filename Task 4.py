# user inputs a number and * will be printed on the same amount of lines entered with 1 * added for each line


while True:
    asterix_amount = int(input("Enter Number:")) # User enters number
    stars = " "
    
    for i in range(0, asterix_amount): # equation for * lines
        stars = stars + "*"
        print(stars)

    start_loop = input("Would you like to enter another number (y/n)?") # asks user if they would like to enter another number
    
    if start_loop == "y": # if user enters y then loop starts again
        continue
    
    else: # if user enters n then loop breaks
        break
