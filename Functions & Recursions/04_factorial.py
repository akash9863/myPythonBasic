n=int(input("Enter the number: "))

# def factorial_iter(n):
#     result=1
#     for i in range(n):
#         result=result*(i+1)
#     return result
# print("Factorial of ",n,"is ",factorial_iter(n))

def factorial_recursive(n):
    if n==1 or n==0:
        return 1 
    return n* factorial_recursive(n-1)
print("Factorial of ",n,"is ",factorial_recursive(n))