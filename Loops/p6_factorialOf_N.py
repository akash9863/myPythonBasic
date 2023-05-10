# n! = 1*2*3*4.....*n

num=int(input("Enter the number: "))
factorial= 1
for n in range(1,num+1):
    factorial= factorial*n
print(f"The factorial of {num} is {factorial}")
    