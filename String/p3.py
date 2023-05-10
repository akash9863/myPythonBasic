# st="This is  a string with  double sapces"
# doubleSpaces = st.find("  ")
# print(doubleSpaces)

#reduceing spaces

st="This is  a string with  double sapces"
doubleSpaces = st.find("  ")
print(doubleSpaces)
st = st.replace("  "," ")
print(st)