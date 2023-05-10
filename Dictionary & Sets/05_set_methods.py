b=set()
#add value
b.add(4)
b.add((1,2,3)) #add as (1,2,3)

# b.add({4:5}) # cannot add dict
# b.add([7,8,9]) # cannot add list

# print(b)

print(len(b)) #length of b

# b.remove(4)
# print(b)


print(b.pop()) # remove randomly
print(b)
b.add(5)
print(b)


# b.intersection({4,7})
