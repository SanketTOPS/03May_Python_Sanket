mydict={}

n=int(input("Enter number of pairs:"))

for i in range(n):
    key=input("Enter Key:")
    value=input("Enter Value:")

    mydict[key]=value

print(mydict)