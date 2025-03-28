####################### For Loop #######################################

name=["Subhash", "Pankaj", "Vivek","Ranjeet"]
for names in name:
    print(names)

#Output : Subhash Pankaj Vivek Ranjeet
########################### Range ###########################################

for x in range(10):
    print(x)
#Output : 0,1,2,3,4,5,6,7,8,9

############################# Range #########################################

for xx in range(3, 10):
    print(xx)
#Output : 3,4,5,6,7,8,9

for xxx in range(2, 10 ,2):
    print("This is range loop using 3 parameter",xxx)

#Output: 2 ,4 ,6 ,8

#Reason: print first value 2 and add into 3rd parameter like here 2 , now 2+2 =4 , again add 4+2=6 and again 6+2=8 &
# now this is response. 10 is not print because 8+2 =10 but still in this function 10 is not printed. Thanks


for number in range(-10,-100,-20):
    print("This is range loop using 3 parameter",number)
#Output: -10,-30,-50,-70,-90

################################## Condition loop ######################################

# #condition loop
color=["Red", "White", "Green","Black"]
for colors in color:
    print(colors)
    if colors == "Green":
        break
# #Output: Red,White,Green

# #conditional loop
a=["Red" , "Green", "Yellow", "Blue"]
b=["Apple", "Orange", "Banana"]

for x in a:
    for y in b:
        print(x ,y)
####################### For Loop #######################################

for value in range(10):
    print(value)
    if value == 5:
        #print("Your Shopping cart is done item:", value)
        break
    #print(value)


for num in range(10):
    if num == 5:
        #print("Your Shopping cart is done item", num)
        break
    #print(num)


for num in range(5):
    if num == 5:
        continue
    #print(num)
#Output: 0 1 2 3 4

#############################Looping Over a Dictionary########################

# person = {"name":"subhash","age":25, "mobile":8878913425 ,  "address": "Nagpur (M.H)"}
#
# for key, value in person.items():
#     print("This is Dictionary for loop:",key,":", value)

#Output:
# This is Dictionary for loop: name : subhash
# This is Dictionary for loop: age : 25
# This is Dictionary for loop: mobile : 8878913425
# This is Dictionary for loop: address : Nagpur (M.H)

#################################### (End For Loop) ##############################

############################# (While loop) #######################################

#break while loop
i = 1
while i < 100:
  #print("Break loop",i)
  if (i == 50):
      #print("Break loop is done:")
      break
  i += 1

#continue while loop
p =0
while p < 10:
    p += 1
    #print("loop is working:", p)
    if p == 5:
        continue
    #print("Continue loop is working:", p)

#continue while Simple loop
color = ["Red","Green", "White", "Blue"]
c = 0
while c < len(color):
    #print("This is a best color names",color[c])
    c +=1


############# Password validation ##############
# email="subh@gmail.com"
# password = "1234"
# attempts = 3
#
# while attempts> 0:
#      user_input_email= input("Enter your email here: ")
#      user_input_password = input("Enter your password here: ")
#      if ((user_input_email == email) and (user_input_password == password)):
#          print("Your have successfully login...!!")
#          break
#      else:
#          attempts -= 1
#          print(f"Wrong credentials ! {attempts} attempts left.")
#      if attempts==0:
#          print("Access denied!")
####################################################################


