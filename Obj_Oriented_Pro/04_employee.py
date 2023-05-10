class Emplyee:
    company = "Google"
    salry = 100

akash = Emplyee()
akash.salary = 1000

siam = Emplyee()
siam.salary = 500

print(akash.company)
print(siam.company)

Emplyee.company = "YouTube"

print(akash.company)
print(siam.company)
print(akash.salary)
print(siam.salary)