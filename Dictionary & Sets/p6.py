favLang={}
a= input("Enter ut fav language Akash: ")
b= input("Enter ut fav language Siam: ")
c= input("Enter ut fav language Rakib: ")
d= input("Enter ut fav language Nahid: ")

#favLang["Akash"]=a
#favLang["Saim"]=b
#favLang["Rakib"]=c
#favLang["Nahid"]=d

updateDict= { 
    "Akash": a,
    "Siam": b,
    "Rakib": c,
    "Nahif": d
}

favLang.update(updateDict)
print(favLang)