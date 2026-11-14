#list

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes", "Papaya"]
print("your elements are: ", fruits)
print("first element: ", fruits[0])
print("last ellement:", fruits[-1])


#append 
#append is use to add element end of the list
fruits.append("Kiwi")
print(fruits)

#insert
#insert is used to add elements (between list)
fruits.insert(2, "Pineapple")
print(fruits)

#pop
fruits.pop(0)
print(fruits)


#remove
#remove is used to remove element from an element
fruits.remove("Pineapple")
print(fruits)


#slicing
print("Sliced elements : ", fruits[1:4])
print(fruits[:5])

#Extend 
more_fruits = ["Guava", "Watermelon"]
fruits.extend(more_fruits) # extend is use to add multiple values at the end 
print(fruits)
