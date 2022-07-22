a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))

if a!=0 and b!=0: #root condition
    if a<b: #child condition
        a+=b #a=a+b
        print("Sum:",a)
    else:
        a*=b #a=a*b
        print("Mul:",a)
else:
    print("Error...Plz input proper value!")




