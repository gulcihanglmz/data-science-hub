import time

print(time.time())

#***
print("Strftime : ")
print(time.strftime("%d:%m:%Y  %H:%M:%S %p"))

#sleep
print("Started")
time.sleep(3)
print("Terminated")

#time to complete a task – to measure productivity(algorithm)
starting = time.time()
list1 = []
for i in range(10000000): #second
    list1.append(i)
finish = time.time()
print(finish-starting) #how much time has passed


#current date
print("Current time")
print(time.ctime())

#until starting date - 10000 second later
print(time.ctime(10000))
print(type(time.ctime()))


#time tupple - localtime()
print("Local time : ",time.localtime())

#To convert the time tupple into a format we can read
time1 = time.localtime()
time2 = time.asctime(time1)
print(time2)

