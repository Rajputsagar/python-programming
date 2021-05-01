a = int(input("enter lower range:"))
b = int(input("enter upper range:"))
for num in range(a, b+1):
    temp = num 
    sum = 0
    n = temp % 10
    sum = sum + n**3
    temp = temp // 10
if num == sum:
    print(num)
        

