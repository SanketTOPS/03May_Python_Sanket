fl=open("stdata.txt","r")

# stid=input("Enter ID:")
# stnm=input("Enter Name:")
# stsub=input("Enter Subject:")

# fl.write(f"Student ID:{stid}\nStudent Name:{stnm}\nStudent Subject:{stsub}")

#print(fl.read())


#dt=fl.readlines()
#dt.reverse()
#print(dt)

#print(fl.read())
#print(fl.readline())
ln=fl.readlines()[::-1]

for i in ln:
    print(i)