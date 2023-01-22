def get_combined_dict(my_dict_1, my_dict_2): #define function
    combined_dict = {} #create combined dict list

    for key, value in my_dict_1.items(): #itterate through dict
        if key in my_dict_2.keys(): #if key is contained in both 1 and 2,
            combined_dict[key] = value + my_dict_2[key] #combine value of key in 1 with value of same key in 2, then add to new combined dict
    return combined_dict #return combined dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9} #tests
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)