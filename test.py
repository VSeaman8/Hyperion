"""file = open("your_calculations.txt","w")
name = input("what is your name?")
file.write(name)
file.close()"""

file = open("your_calculations.txt", "r")
lines = file.readlines()

for line in lines:
    temp = line.strip()
    temp = temp.split(", ")

    print(temp[0])
file.close()