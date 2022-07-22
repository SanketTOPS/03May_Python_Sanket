def getdata(id,name,sub='Python',city='Rajkot'):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)
    print("City:",city)

#getdata(101,'Sanket','JAVA') #possitional arguments

#getdata(id=101,name='Nirav') #keyword arguments

stid=input("Enter ID:")
stnm=input("Enter Name:")

getdata(id=stid,name=stnm)