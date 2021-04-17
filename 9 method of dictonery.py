myDict = {
    "fast":"in a quick manner",
    "harry":"a coder",
    "marks":[1,4,7],
    "anotherdict":{'harry':'player'},
    1:2
}

# dictonery methods
'''print(list(myDict.keys()))  # print the key of the dictonery
print(myDict.values())      # print the value of the dictonery
print(myDict.items())       # print the (key,value) for all contents of the dictonery
print(myDict)
updateDict = {
    "mukul":"my friend",
    "tanisha":"my friend",
    "harry":"a dancer",
}
myDict.update(updateDict)  # update the dictionery by adding key-value pair from updateDict
print(myDict)

print(myDict.get("harry"))   # print value associated with key "harry"
print(myDict("harry"))       # print value associated with key "harry"'''

#the difference between .get and [] syntax in dictionery?
print(myDict.get("harry 2"))  # return none as harry2 is not present in dictionery
print(myDict("harry 2"))      #throw an error as harry2 is not present in dictionery