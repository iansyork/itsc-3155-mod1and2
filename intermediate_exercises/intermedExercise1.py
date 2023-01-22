def get_unique_list(my_list): #define unique list function with input from my_list

    newlist = [] #create new list to return
    for number in my_list: #itterate though list
        if number not in newlist: #add to new list if not already present
            newlist.append(number)
    
    return newlist #retrun new list

my_list = [1, 2, 3, 2, 1, 4] #test
unique_list = get_unique_list(my_list)
print(unique_list)
