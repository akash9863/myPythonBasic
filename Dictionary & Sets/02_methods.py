myDict = {
    "fast" : "In a Quack Manner",
    "akash" : "A coder",
    "marks" : [1,2,5],
    "anotherDict" : {"siam": "My brother"},
    1:2
}
# print(myDict.keys()) # print keys of dictionary
# print(myDict.values()) # print value
# print(myDict.items())

updateDict= { 
    "lovish": "Friends"
}
myDict.update(updateDict)

print(myDict.get("akash"))
print(myDict["akash"])
# print(myDict.get("akash2")) # return none as not present
# print(myDict["akash2"]) #shows an error