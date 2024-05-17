print('Do anything')
print("Do anything")
print('Do\' anything')  #escape character=\
print('''
      Do 
      anything
      !!
      ''')
print("Do\nanything")  

message = "Do anything"
print(message)
print(message*3)
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.startswith("D"))  #true-false
print(message.endswith("g"))
print(message.endswith("G"))    #case sensitive
print(len(message))             



print(message[0])
print(message[-1])
print(message[0:3])
print(message[::2])
print(message[::-1])



m1 = "Do"
m2="anything"
print(m1+m2)
print(m1+" "+m2)

print("{} {}".format(m1,m2))   #format
print(f"{m1} {m2}")            #f-string



num1 = 5
num2 = 4.8
num3 = 5 ** 8
num4 = "5"

print(type(num1))
print(type(num2))
print(type(num3)) 
print(abs(-2))
print(round(num2))
print(type(num4))
print(num1 == num4) #false

num5 = int(num4)
print(num1 == num5) #true



list1 = ["white","black","blue"]
list2 = ["gray","red"]

print(type(list1))
print(list1)
print(len(list1))
print(list1[0])
print(list1[1:])
print(list1[0:2])
print(list1[1:2])
print(list1[::2])

list1.append("brown")      #append = adding element
print(list1)

list1.insert(0,"purple")   #insert = adding element with parameter
print(list1)

list1.extend(list2)
print(list1)

list1.remove(list1[1])
print(list1)

list1.pop()
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

for color in list1:
      print(color)
      

print(list(enumerate(list1)))             #enumarate

print(list(enumerate(list1,start=1)))
 
print("blue" in list1) #true - false

#to convert text file
stringLİst1 = " ".join(list1)             #join
print(stringLİst1)
print(type(stringLİst1))

stringLİst1 = ",".join(list1)             #join
print(stringLİst1)

stringLİst1 = "-".join(list1)             #join
print(stringLİst1)


colors = stringLİst1.split("-")           #split 
print(colors)


#tuple
tuple1 = ("white","black","blue","gray","red")  #tupple cannot be update (tuple1[1] = "yellow" )
print(len(tuple1))
 

#set
set1 = {"white","black","blue","gray"}    #the order doesn't matter in sets
print(set1)
print(type(set1))
print(len(set1))

set1.add("red")
print(set1)

set1.remove("gray")
print(set1)

set1.discard("green")     #discard = When we try to delete an element that does not exist and we do not want to get an error
print(set1)

set1 = {"white","black","blue","gray"}
set2 = {"red", "green", "blue", "yellow"}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))


emptyLİst1 = []
emptyLİst2 = list()

emptyTuple1 = ()
emptyTuple2 = tuple()

emptySet1 = set()

#distionary
emptyDict1 = {}         #this declaration is not a set, it's dictionary

my_dict = {             #key : must be an int or string
    "name": "John",  
    "age": 30,
    "city": "New York"
}

print(my_dict)
print(my_dict["age"])
print(my_dict["name"])

my_dict["name"] = "maria"
print(my_dict["name"])

my_dict.update({"age": 20 , "city": "İstanbul"})
print(my_dict)

my_dict["id"] = 5548
print(my_dict)

del my_dict["id"]
print(my_dict)

for x in my_dict:  #print "key"
      print(x)

for x in my_dict:  #print "value"
      print(my_dict[x])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for k in my_dict.items():
      print(k)


for k,v in my_dict.items():
      print(k,v)

print(my_dict.get("id"))     #None
print(my_dict.get("id","Does not exist"))  #Does not exist / write a message 



