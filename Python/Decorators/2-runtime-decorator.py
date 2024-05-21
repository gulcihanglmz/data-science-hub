import time

#to calculate runtime

def calculate_runtime(funct):
    def wrapper(*args, **kwargs):
        started = time.time()
        funct(*args, **kwargs)
        terminated = time.time()
        print(f"The processing time is : {terminated-started} second")
    return wrapper
 
 
@calculate_runtime
def square(list):
    for i in list:
        print(i*i)
    
    
@calculate_runtime
def cube(list):
    for i in list:
        print(i*i)
  
  
@calculate_runtime
def summation(a,b):
    time.sleep(1)
    return a+b


square(range(100000))

