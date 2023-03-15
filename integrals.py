#Import utilized libraries
import math 
import time

def evaluate_integral(n):
    st = time.time() #start the timer
    #Declare the variables
    N = n
    h = 2 / N 
    I = 0 
    
    for k in range(1, N + 1): 
        xk = -1 + h * k 
        yk = math.sqrt(1 - xk ** 2) 
        I += h * yk
    et = time.time() #stop the timer
    #Calculate the execution time
    elapsed_time = et-st
    #Print the results
    print("Execution time: ", elapsed_time)
    print("Approximate value of integral with N =", N, "slices:", I) 
    print("Exact value of integral:", math.pi / 2)
    #Checks whether the elapsed time is greater than or equal to 1
    if(elapsed_time>=1):
        return False
    else:
        return True

isValid = True
n = 100
# Loop until execution time is greater than 1 
while(isValid): 
    isValid = evaluate_integral(n)
    n*=10 #multiply the paramater input by 10




    
    

