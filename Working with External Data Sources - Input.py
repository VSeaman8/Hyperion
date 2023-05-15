# program to print out 2 seperate lists from DOB.txt
# opens DOB.txt
with open("DOB.txt", "r") as file:
    
    names = []
    birthdays = []
   
# splits DOB.txt and appends information to either names or birthday list
    for line in file:
       sentance = line.split()
       name =" ".join(sentance[:2]).replace(",", "")
       birthday = " ".join(sentance[2:]).replace(",", "")
       names.append(name)
       birthdays.append(birthday)

# prints names from DOB.txt
    print("Names:")
    for name in names:
        print(name)

    print()

# prints birthdays from DOB.txt
    print("Birthdays:")
    for birthday in birthdays:
        print(birthday)
