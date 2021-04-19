a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))
if(a>b and a>c):
   print("a is greater")
elif(a<b and b>c):
   print("b is greater")
elif(a<c and b<c):
    print("c is greater")      