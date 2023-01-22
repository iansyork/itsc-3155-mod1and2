userInput = raw_input("Enter a string: ") #get user to input string

def count_lowercase(userInput): #define function
    count = {} #define new dict
    for letter in userInput: #iterate through user input
        if letter.islower(): #determine if letter is lowercase
            if letter not in count: #if lowercase and not in count, add to count as 1
                count[letter] = 1
            else:
                count[letter] += 1 #if lower and in count, add +1 to count
    return count

print (count_lowercase(userInput))

