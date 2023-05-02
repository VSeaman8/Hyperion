
""" This code will calculate if a triathete has passed the qualification time and which qualification bracket they will be in.
User will need to enter their swimming, cycling and running time, which will then calculate if they have qualified and which bracket they will be in.
They will get one of 4 options
Provincial Colours = if less than 100 minutes
Prvincial Half Colours = between 101-105 minutes
Provincial Scroll = between 106-110 minutes
No Award = Any time above 110 minutes
"""
swimming_time = int(input("How many minutes did you swim?")) # Q How many minutes did you swim?
cycling_time = int(input("How many minutes did you cycle?")) # Q How many minutes did you cycle?
running_time = int(input("How many minutes did you run?")) # Q How many minutes did you run?

Total_time = swimming_time + cycling_time + running_time # total time = swimming time + cycling time + running time

if Total_time <=100: # If users total time is less than 100 minutes then they have won Provincial Colours
    print("You have qualified. Congratulations you have won the Provincial Colours")

elif Total_time >= 101 and Total_time <= 105: # If users total time is between 101-105 minutes then they have won Provincal Half Colours
    print("You have won Provincial Half Colours")

elif Total_time >= 106 and Total_time <= 110: # If users total time is between 106-110 minutes then they have won a Provincal Scroll
    print("You have won the Provincial Scroll")

else: 
    print("Sorry No award!") # If user has more than 110 minutes then they have no award
