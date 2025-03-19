#An empty my_list list
my_list = []
print(my_list)

#Appending elements to my_list list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Inserting elements to my_list list
my_list.insert(1,15)
print(my_list)

#Extending elements to my_list list
new_list=[50,60,70]
my_list.extend(new_list)
print(my_list)

#Removing elements from my_list list
my_list.remove(my_list[-1])
print(my_list)

#Sorting elements in my_list list
my_list.sort()
print("Sorted in ascending order:", my_list)

#Printing the index value of an element in a list
element = 30
index = my_list.index(element)
print(f"The index of element {element} is: {index}")







