from itertools import count

print("New Topic: list,Tuples")

#1.List==> Lists are used to store multiple items in a single variable.

color =["Red", "Blue","Green","Yellow"]
#print("This is your list of color", color) //Output:  ['Red', 'Blue', 'Green', 'Yellow']

#using loop print
# for colors in color:
#     #print("This is print data using loop",colors)

#*****************************************************************************************************#

#2.Tuples==> Tuples are used to store multiple items in a single variable.
           #(1). Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
           #(2). Once tuples is created, you can not change values. Tuples are unchangeable, or immutable as it also is called.

        #Syntax: mytuple = ("apple", "banana", "cherry")

#Example 1:
school=("SSVM","PMSC","SBMN","SSMV")
#print("Tuple is print",school)

# for sch in school:
#     #print("Uisng loop is print",sch)

#Example 2: Convert Into a List::==> First convert into list and then add value in tuples
fruits= ("orange", "mango","banana")
y=list(fruits)
#print("Convert first into list",y) // Output: ['orange', 'mango', 'banana']

y.append("ppaya")
fruits=tuple(y)
#print("Now convert again in tuples",fruits) //Output: ('apple', 'banana', 'cherry', 'mango', 'subhash')

#Example 3: Add tuple to a tuple::==> You are allowed tuple to tuple, so if you want to add one or more item,
# create a new tuple with the item(s), and add it to the existing tuple:

this_tuple=("apple","banana","cherry")
y=("mango","subhash")
this_tuple +=y
#print("This is new updated tuple",this_tuple) //Output:  ('apple', 'banana', 'cherry', 'mango', 'subhash')

#Example 4: join tuple
tu1=(1,2,3)
tu2 =(4,5,6)
total=tu1+tu2
#print("Join Tuple",total) //Output: (1, 2, 3, 4, 5, 6)

#Example 5 : Multiply Tuples:: ==> If you want to multiply the content of a tuple a given number of time ,# you can used * operato:

numb=("subhash","vivek", "pankaj")
Multiply = numb * 5
print("This is multiple data",Multiply)

#Python has two built-in methods that you can use on tuples.
#1. count()  2.index()

#1.count() Tuple
#Syntax: tuple.count(value)

number=(1,2,3,4,5,6,7,5)
x=number.count(5)
#print("Tuple count",x) Output: 2

#1.index() Tuple
#Syntax: tuple.index(value)

number=(1,2,3,4,5,6,7,5,2)
xx=number.index(2)
print("Tuple index",xx)
#*****************************************************************************************************#

#3.Set==> Sets Python used to store collections of data.

#Syntax: myset = {"apple", "banana", "cherry"}

#Important: (1) Sets cannot have two items with the same value. OR Duplicate values will be ignored:


name = { "subhash","vivek", "pankaj","pankaj"}
print("Set is used",name)
#Output:  {'subhash', 'vivek', 'pankaj'} //Duplicate values are ignored Output: {'pankaj', 'vivek', 'subhash'}


for names in name:
    print("This is set",names)
#Output:  'subhash', 'vivek', 'pankaj' //Duplicate values are ignored


#Add an item to a set, using the add() method:
name = { "subhash","vivek", "pankaj","pankaj"}
name.add("Ravi")
#("This is update value using dd function",name) //Output: {'pankaj', 'vivek', 'subhash', 'Ravi'}



#Remove an item to a set, using the remove() method:
name1 = { "subhash","vivek", "pankaj","pankaj"}
name1.remove("vivek")
#print("This is remove value using dd function",name1) //Output: {'pankaj','subhash'}


# To add items from another set into the current set, use the update() method. //Add two variable
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
#print("This is output of Update:",thisset) //Output: {'papaya', 'banana', 'mango', 'cherry', 'apple', 'pineapple'}


# difference()  : Return a set that contains the items that only exist in set x, and not in set y:
x = {"subhash", "vivek", "pankja"}
y = {"sandeep", "ranjeet", "subhash"}

#z=y.difference(x)  //Output: {'ranjeet', 'sandeep'}

#print("This is different:", z)

#*****************************************************************************************************#

#3.Dictionaries==> Dictionaries are used to store data values in key:value pairs.

personalDetails = {
  "name": "Subhash",
  "surname": "Paradkar",
  "dob": 1990,
  "mobile": 8878913425
}
#print("This is Dictionaries :", personalDetails) //Output: {'name': 'Subhash', 'surname': 'Paradkar', 'dob': 1990,'mobile': 8878913425}


for x,y in personalDetails.items():
    print(f"What is your name {x} ? Answer : {y}")


#Adding Item: Added new item which is added in function
personalDetails["color"]="white"
#print("This is Dictionaries Adding Function :", personalDetails) // Output:{'name': 'Subhash', 'surname':
# 'Paradkar', 'dob': 1990, 'mobile': 8878913425, 'color': 'white'}

#Function: pop() Remove form Dictionaries which is call in pop()
personalDetails.pop("mobile")
#print("This is remove form mobile:",personalDetails) //Output:  {'name': 'Subhash', 'surname': 'Paradkar',
# 'dob': 1990, 'color': 'white'}

#Function: popitem() Remove last inserted item from Dictionaries
personalDetails.popitem()
#print("This is remove last inserted item:",personalDetails) //Output:{'name': 'Subhash', 'surname': 'Paradkar', # 'dob': 1990}

#Function: del() Remove last inserted item from Dictionaries
del personalDetails["name"]
#print("This is delete item:",personalDetails //Output:{'surname': 'Paradkar', 'dob': 1990}


