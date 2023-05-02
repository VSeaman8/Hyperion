
# program for user to register students ID for exam

try:
        registration = open("reg_form.txt", "w") # open registration txt document

        many_stu = int(input("How many students are registering? ")) # How many students are being registered?

# loop that asks for students ID number, saves to registration.txt (with sign in space for student)

        for num in range(many_stu):
            while True:
                stu_id = input("What is your Student ID number? ")

                if len(stu_id) != 5:
                    print("Invalid Student ID number! Please reenter the correct ID ")
                else:
                    break
                
            registration.write(stu_id + "\n")
            registration.write("Sign in here: ______________________ \n\n")
            
            
        registration.close()

        print("Congratulations you have registered correctly!") 

# error handling

except ValueError as e:
    print("Error", e)
    
except IOError:
     print("Error: Unable to open or write to file. Please contact your admin")