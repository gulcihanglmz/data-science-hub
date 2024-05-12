#If - Elif - Else
if True:
    print("Condition is true")

color = "white"
if color == "white":
    print("Color = white")
elif color == "blue":
    print("Color == blue")
else:
    print("None")
    

a = 5 
b = 10
c = 15 

#or
if a > b or c > b :
    print("Condition is true")
else:
    print("Condition is false")
    

#and
if b > a and c > b :
    print("Condition is true")
else:
    print("Condition is false")
  

#in 
list1 = ["white","black","blue"]
if "white" in list1:
    print("'white' is exist")
else:
    print("Color does not exist")
    
    
#not
list1 = ["white","black","blue"]
if not color in list1:
    print("'white' is exist")
else:
    print("Color does not exist")


#is (identical = in the same location in memory)

a = "Python"
b = "Pytho"
b += "n"
print(a)
print(b)

if a == b :           #a == b
    print("a = b")
else:
    print("a != b")
 

if a is b :           #a != b
    print("a = b")
else:
    print("a != b")  
    print(id(a))     #location in memory
    print(id(b))     #location in memory
    
     
  
#For Loop
for number in range(0,5):  #5 not included
    print(number)


for i in range(0,50,5):  
    print(i)


num = 1
for number in range(1,5):
    num *= number
    print(num)
print("Result : ",num) 


listNum = [1,2,3,4,5,6,7,8,9]
for i in listNum:
    if i == 3:
        print("Until 3 and break")
        break
    else:
        print(i)
        


listNum = [1,2,3,4,5,6,7,8,9]
for i in listNum:
    if i == 3:
        print("Skip 3 and continue")
        continue
    else:
        print(i)
        
             
list2 = range(50)
for i in list2:
    if i %3 != 0 :
        continue
    if i == 24:
        break
    print(i)

    
    
#while loop

count = 0
while count < 5:
    print("Count is", count)
    count += 1


i = 1
while True:
    print(i)
    i += 1
    if i == 10:
        break
    
while True:
    if i %2 == 0:
        i +=1
        continue
    print(i)
    i += 1
    if i == 100:
        break
    
    
#input
number = input("Enter a number : ")
print(type(number))    #string

number = int(number)
print(type(number))


number = int(input("Enter a number : "))
fact = 1
for i in range(1,number+1):
    fact *= i
print(fact)


number = int(input("Enter a number : "))
fact = 1
i = 2
while i<=number:
    fact *= i
    i += 1
print(f"{number}! = {fact}")

#prime number
number = int(input("Enter a number : "))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#divisor number of a number
number = int(input("Enter a number : "))
divisor_number = 0
for i in range(1,number+1):
    if number %i ==0:
        divisor_number+=1
print(f"Divisor number of {number} : {divisor_number}")
     
       
#the sum of the digits of a number    
number = int(input("Enter a number : "))
str_number = str(number)
sum = 0
for num in str_number:
    sum += int(num)
print(sum)


#min - max
numberList = []
for i in range(5):
    number = int(input("Enter a number : "))
    numberList.append(number)
print(f"Max number : {max(numberList)}")
print(f"min number : {min(numberList)}")

#squareroot
number = int(input("Enter a number : "))
squareroot = number ** 0.5
if squareroot == int(squareroot):
    print("perfect square")
else:
    print("not a perfect square" )


#number of same letters in a string
string = input("Enter a string : ")
dict = dict()
for letter in string:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1
for letter,number in dict.items():
    print(letter , number)
    


text = input("Enter a string : ")
text2 = ""
for letter in text:
    if letter == "a":
        text2 += "A"
    else:
        text2 += letter
print(text2)
        
    
