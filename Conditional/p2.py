sub1=int(input("ENter first subject Number: "))
sub2=int(input("ENter second subject Number: "))
sub3=int(input("ENter third subject Number: "))

if(sub1<33 or sub2<33 or sub3<33):
    total= (sub1+sub2+sub3)
    per1= (total/3)
    print("Fail\nYour percantage is: ",per1)
else:
    total= (sub1+sub2+sub3)
    per2= (total/3)
    print("Pass\nYour percentage is: ",per2)