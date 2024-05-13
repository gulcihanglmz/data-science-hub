import random 

#in the range of 0-1 ->> random() fonction
for i in range(10):
    print(random.random())
    
 
#in the range of decimal ->> uniform() fonction
for i in range(10):
    print(random.uniform(10,20))
    
#to generate int numbers ->> randint() / randrange() fonctions
for i in range(10):
    print(random.randint(10,20))  #randint = including two borders (10,20)

for i in range(10):
    print(random.randrange(1,10,2))  #randrange = second side not included (10,20)
        
#choice
list1 = ["white","black","blue","red"]
print(random.choice(list1))

#shuffle
list1 = ["white","black","blue"]
random.shuffle(list1)
print(list1)

#sample = to randomly select 3 items
list1 = ["white","black","blue"]
print(random.sample(list1,3))

#a dice thrown 1000 times
dices = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for i in range(1000):
    dice = random.randint(1,6)
    dices[dice] += 1
for dice in dices:
    print(f"Probability of coming {dice} : {dices[dice]/1000}")
    


six_six = 0
number_try = 0
while True:
    number_try += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == 6 and dice2 == 6:
        six_six += 1
    if six_six == 10:
        print(f"The dice were thrown {number_try} times to get 6-6.")
        break

