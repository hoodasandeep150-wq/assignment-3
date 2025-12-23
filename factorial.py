def factorial(num):
    
    if num==1 or num==0:
        return 1 
    else:
        fact=num*factorial(num-1)
    return fact  
num=int(input('enter a number : '))  
print(f"factorial of {num} is {factorial(num)}") 