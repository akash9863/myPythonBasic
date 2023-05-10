mydict= {
    "pankha": "Fan",
    "dibba": "Box",
    "lathi": "Stick"
}
print("Options are: ",mydict.keys())
a=input("Enter the word: ")
print("The meaing is: ", mydict.get(a))