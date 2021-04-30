def feh(cel):
    return (cel * (9/5))+32
c = int(input("enter the temp in celcius"))
f = feh(c)
print("the temp is " + str(f))   