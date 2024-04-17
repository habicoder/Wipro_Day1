my_list = [1, 2, 3, 4, 5]  
new_value = int(input("Please enter the new value:\n"))
index = int(input("Please enter the index where you would like to place the above value:\n"))


if len(my_list) >= index+1: 
    my_list[index] = new_value  
    print("Modified list:", my_list)
else:
    print("Size of list is smaller than the index specified.")