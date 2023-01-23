
while True:
    try: 
        int1 = int(raw_input("Intput int 1: ")) #assign input to variable
    except ValueError: #test if input is an int
        print("Invalid input. Please enter an int.") #error message if input isn't an integer, continue while loop until input is an integer
        continue
    break

while True:
    try: 
        int2 = int(raw_input("Intput int 2: "))
    except ValueError:
        print("Invalid input. Please enter an int.")
        continue
    break

while True:
    try: 
        int3 = int(raw_input("Intput int 3: "))
    except ValueError:
        print("Invalid input. Please enter an int.")
        continue
    break

while True:
    try: 
        int4 = int(raw_input("Intput int 4: "))
    except ValueError:
        print("Invalid input. Please enter an int.")
        continue
    break

while True:
    try: 
        int5 = int(raw_input("Intput int 5: "))
    except ValueError:
        print("Invalid input. Please enter an int.")
        continue
    break

final = int1 + int2 + int3 + int4 + int5 #calculate total from input

print("Your sum is: " + str(final)) #display total


