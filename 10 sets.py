# creating a empty set 
b = set()
print(type(b))
# adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add((4,5,6))  # cannot add list and dictionary to a set
print(b)
print(len(b))    # print the length of the set
b.remove(5)      # remove 5 from set
print(b)  
print(b.pop())    # it remove a element randomly from the set
print(b)
print(b.clear())   # it clear the set
print(b)
print(b.union({2,6}))  # union of two sets
print(b.intersection({4}))   # intersection of two sets