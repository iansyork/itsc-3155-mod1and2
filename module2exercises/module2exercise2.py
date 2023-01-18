string1 = input('Enter a string: ')

string1 = string1.replace(" ","") #remove spaces from string

uppercase = "" #declare uppercase string
lowercase = "" #declare lowercase string

for x in string1:
    if x.isupper(): #detect if letter is upper
        uppercase += str(x) #add to uppercase string
    elif x.islower(): #detect if letter is lower
        lowercase += str(x) #add to lowercase string

output = lowercase + uppercase #add strings for result

print(output)

