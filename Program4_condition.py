#************************* If & else #*************************

a = int(input("Entre your age: "))
print("Your age is:", a)
if(a>18):
    print("You can drive Subhash")
else:
    print("You can not drive subhash")

## Important===>  Before print blank space is called Indentation in python.

#*************************If & else #*************************


#************************* If & el & else #*************************

## Important===> here we are using el Not else

num=int(input("Enter a number: "))

if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
elif(num ==999):
    print("Number is special")
else:
    print("Number positive ")

#************************* If & el & else#*************************


#*************************Nested Loops #*************************
num1 = 18
if (num1 < 0):
    print("Number is negative.")
elif (num1 > 0):
    if (num1 <= 10):
        print("Number is between 1-10")
    elif (num1 > 10 and num1 <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
#************************* Nested Loops #*************************

############################## Match case Statement#############################

#Match Case Statement: The match-case statement in Python (introduced in Python 3.10) is similar to switch-case in other languages.
# It allows you to match a variable against multiple patterns efficiently.
