letter = ''' Dear <|Name|>,
 You are slected! 
 Date: <|Date|> '''
name= input("Enter your Name: \n")
date= input("Enter Date: \n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)