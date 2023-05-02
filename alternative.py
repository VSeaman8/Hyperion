# program to alternate upper and lower cases and then to join the sentance together
string_example = "This is an example varible!"
final_example = ""

# turns string_example characters to alternate upper and lower case
for i in range(len(string_example)): 
    if i % 2 == 0:
        final_example += string_example[i].upper() # upper case code

    else:
        final_example += string_example[i].lower() # lower case code
   

print(final_example) # prints result of if/else statement

# turns final_example words into alternate upper and lower case
split_example = string_example.split()
final_split = [] 

for i in range(len(split_example)):
    if i % 2 == 0:
        final_split.append(split_example[i].upper()) # upper case code
    else:
        final_split.append(split_example[i].lower()) # lower case code

final_string = ' '.join(final_split)
print(final_string) # prints result of final_string