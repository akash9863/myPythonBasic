def remove_and_strip(string,word):
    newStr=string.replace(word,"Good Boy")
    return newStr.strip()

this="    Akash is a Coder     "
n=remove_and_strip(this,"Coder")
print(n)





# print(this)
# print(this.strip())