# program for user to calculate amount of interest they would earn on investment (either simple or Compound interest)
# or how much they would have to pay on a home loan (bond)
import math # import math module

# info to user on investment/bond and a choice to calculate which they want to do
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

option = input("Enter either investment or bond from the menu above to proceed:").lower().strip()

while True:
    if option == "investment": # If investment option is chosen
        deposit = int(input("How much money do you want to deposit?")) # Q for user to input their deposit
        interest_rate = float(input("Enter interest rate (%):"))/100 # Q for user to input their interest rate
        years = float(input("How many years?")) # Q for user to input the amount of years
        interest_type = input("Which interest do you want simple or compound?") # user option for interest type - simple or compound

        if interest_type.lower().strip() == "simple": # If user choses simple interest
            P = deposit
            r = interest_rate
            t = years

            A = P*(1 + r*t) # Formula for working out simple interest
            print("Your simple interest is", A) # Simple interest result printed
            break
            
        elif interest_type.lower().strip() == "compound": # If user choses compound interest
            P = deposit
            r = interest_rate
            t = years
            
            A = P * math.pow((1+r),t) # formula for working out compound interest
            print("Your compound interest is", A) # Compound interest result printed
            
        else:
            option = (input("error please enter simple or compound interest:")) # error if compound or simple is incorrectly typed


    elif option == "bond": # If Bond is chosen
        Present_Value = int(input("What is the present value of the House?")) # Q for user to input present value of house
        bond_interest = float(input("What is the interest rate (%)?"))/100 # Q for user to input interst rate
        number_months = int(input("Number of monthly repayments?")) # Q for user to input amount of montly repayments

        house = Present_Value
        i = bond_interest/12
        n = number_months
        repayment = (i * house)/(1 - (1+ i)**(-n)) # formula for working out bond
        print("Your repayment would be:", repayment) # result of bond printed
        break

    else:
         option = input("error please input bond or investment:").lower().strip() # error if user typed in something different
    
   
        