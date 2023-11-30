string=input("enter a string:")

if len(string)<=2:
    print("erroor...")
else:
    newstring=string[:2] + string[-2:]

print("newstring:",newstring)