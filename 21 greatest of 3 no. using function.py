def maximum(num1, num2, num3):
    if(num1>num2 and num1>num2):
        return num1
    elif(num1<num2 and num2>num3):
        return num2
    elif(num1<num2 and num2<num3):
        return num3
x = int(input("first number: "))
y = int(input("second number: "))
z = int(input("third number: "))       
max = maximum(x, y, z)
print("the maximum value is :" + str(max))
