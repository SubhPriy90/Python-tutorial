print("Start your exercise tutorial : Data Structures")

##****************************************Data Structures*******************************#

#More on Lists

###Append function in Python###

##Defination: In Python, you can use the append() method to add an element to the end of a list. Here's an example:
##syntex: list_name.append(item)

numbers = [1,2,3]
numbers.append(4)
numbers.append("Hello subhash")
numbers.append(5.20)

list1 =[1,2,3]
list2 =[4,5,6]
list1.append(list2)

#print("Append function in python list1", list1)
#print("Append function in python", numbers)
#****************************************************************************#
###extend function in Python###
##Defination: In Python, the extend() method is used to add multiple elements from an iterable (such as another list, tuple, or string) to the end of an existing list.
##syntex: list_name.extend(iterable)

fruits= ["banana", "orange"]
fruits.extend(["mango","dragon fruits","1.0",10 ])

#print("extend function in python", fruits)
#****************************************************************************#

#function: list.insert(index, element)
##Defination: The insert() method in Python is used to insert an element at a specific index in a list.
##syntex: list_name.insert(index, element)

#Example 1:  Inserting an Element at a Specific Position(Here Index2 pe 3 add karna hai accroding to syntex)

type1=[1,2,4,5,6]
type1.insert(2,3)
#print("Insert data",type1)
#Output: [1,2,3,4,5,6]

#Example 2: Inserting at the Beginning (Index 0)

days =["tus","wed","fri"]
days.insert(0,"mon")
#print("Insert data of 0 indexing", days)
#Output: ["mon","tus","wed","fri"]


#Example 3: Inserting at the last length (len)
days.insert(len(days),"sunday")
#print("Insert data of last length", days)
#Output: ["tus","wed","fri","sunday"]


#Example 3: Inserting at the last length (len)

num=[10,15,20,25]
num.insert(-2,30)
#print("Insert Data length of -2",num)
#Output: [10, 15, 30, 20, 25]
#****************************************************************************#
#function: list.remove(x)

##Defination: The remove() method in Python removes the first occurrence of the specified element x from a list.
#Example 1: Removing an Element

fruitsA = ["apple", "banana", "cherry", "peru"]
fruitsA.remove("banana")
#print("Remove Number", fruitsA)
#Output:Filter data: ["apple", "cherry", "peru"]

coll = [1,2,3,4,5,6]
coll.remove(4)
#print("Remove Number", coll)
#Output:Filter data: [1,2,3,5,6]

#Example 2: Removing Elements from a List in a Loop
item=[1,2,3,2,4,5,2,6,6,"Subhash",5.5]
filter_item =list(filter((lambda y:y !=2 and y !=6),item)) ##Multipal
filter_item =list(filter(lambda y:y !=2,item))             ##Singal
##("Filter data:",filter_item)
#Output:Filter data: [1, 3, 4, 5, 'Subhash', 5.5]

#****************************************************************************#

#function: list.pop([i])

##Defination: The pop() method in Python removes and returns an element from a list at a given index.
#Example 1: Removing an Element

fruits = ["apple", "banana", "cherry"]
fruits.pop()
fruits.pop(0)
#print("Pop function is calling",fruits) #Removing  last elements Or you will give the index of elements
#output: Pop function is calling ['banana'] only banana becase calling last index and also defind 0 index that why

#****************************************************************************#

#function: list.clear()

##Defination: The pop() method in Python removes and returns an element from a list at a given index.
#Example 1: Removing an Element

test= [1,2,3]
test.clear()
#print("Clear function is calling",test)
#Output: Clear function is calling []


list_number = [1,2,3]
del list_number[:]
#print("Del function is calling",list_number)
#Output: Del function is calling []
#****************************************************************************#

#function: list.index(x[, start[, end]])
##Defination:  The index() method is used to find the first occurrence of an element x in a list.It returns the index (position) where x is found.

#Example 1:
col= ["Red", "Green", "Blue","Purple", "Yellow"]
sub=col.index("Blue")
#print("Index of color",sub)

#Example 2:
numbers = [10, 20, 60,30, 40, 20, 50,60,80,40,20]
index = numbers.index(60, 3)  # Start searching from index 3 which us defind in function....60 is find in index 3 se
# aage and get indexing now 60 indexing is: 7
#print("Index start from 2 index:",index)

#uisng if condition get index of your list
list = [1,5,6,9,8,7,2,23]
# i=int(input("Enter your number:"))
# # if i in list:
# #     print("Your enter data index is:",list.index(i))
# # else:
# #     print("Data is not available in List ")
##Output: Your enter data index is: 7 || when you enter 23 which is available in list

#*****************************************************************************************#

#function: list.count(x)
##Defination:  The count() method in Python returns the number of times an element x appears in a list.

#Example 1:
numberData= [10,20,30,10,45,12,10,10,45,20,12,20]
# dataEnter=int(input("Enter your count number:",))
# countData=numberData.count(dataEnter)
# print("My count number is:",countData) #12 type
##Output: My count number is: 2


#Example 2:
numberData_if= [10,20,30,10,45,12,10,10,45,20,20,20]
# dataEnter_if=int(input("Enter your count number:",))
#
# # if numberData_if.count(dataEnter_if)  > 0:
# #     print("This is output",numberData_if.count(dataEnter_if))
# # else:
# #     print(f"'{dataEnter_if}' is not in the list")

#*****************************************************************************************#

#function: list.sort(*, key=None, reverse=False)
##Defination:  The sort() method sorts the elements of a list in place (modifies the original list) in ascending order by default.


#Syntax: list_name.sort(key=None, reverse=False)
    #key (optional): A function that defines a custom sorting order.
    #reverse(optional, default False): If True, sorts in descending order.

#Example 1:

sortNum=[1,5,6,9,4,36,45,65,64,89,98,78,77,89]
#sortNum.sort()   //Output:  [1, 4, 5, 6, 9, 36, 45, 64, 65, 77, 78, 89, 89, 98]----ASC Order
#sortNum.sort(reverse=True) //Output:  [98, 89, 89, 78, 77, 65, 64, 45, 36, 9, 6, 5, 4, 1]----DESC Order
#sortNum= ["boll", "apple","dog","cate",] //Output: ['apple', 'boll', 'cate', 'dog'] ---Sort also string
#sortNum= ["boll", "apple","dog","cate","aeroplane","kite","monkey","am"]  //Output:  ['am', 'dog', 'boll', 'cate',
# 'kite', 'apple', 'monkey', 'aeroplane'] ---Sort also string len

#print("Sort list data is ASC",sortNum)

people= [
    {"name":"subhash","age":"20"},
    {"name":"Suhash","age":"24"},
    {"name":"vivek","age":"21"},
]
people.sort(key=lambda person:person["age"])
#print("Age print ASC Order:",people)

#**************************************************************************************#

#function: list.reverse()
##Defination:  The reverse() method reverses the elements of a list in place, meaning it modifies the original list # instead of creating a new one.
#Syntax:list_name.reverse()

#Example 1:

sortNum1=[1,5,6,9,4,36,45,65,64,89,98,78,77,89]
sortNum1.reverse() #sortNum1.reverse()  #Output: [89, 77, 78, 98, 89, 64, 65, 45, 36, 4,# 9, 6, 5, 1]

sortNum2=["boll", "apple","dog","cate",]
sortNum2.reverse() #Output :  ['cate', 'dog', 'apple', 'boll']

#print("Data is reverse:",sortNum2)

#**************************************************************************************#

#function: list.copy()
##Defination:  The copy() method creates a shallow copy of a list. It returns a new list with the same elements as the original but does not modify the original list.
#Syntax: new_list = list_name.copy()

#Example 1:

original = [1, 2, 5, 4, 5,4 ,6, 9 ,8]
copied = original.copy()
print("New original copy",copied)

copied.sort()
print("Sorting ASC",copied)

