def getdata(data):
    print("ID:",data["id"])
    print("Name:",data["name"])
    print("Subject:",data["sub"])
    print("City:",data["city"])

#getdata({'id':12,'name':'sanket','sub':'php','city':'ahmedabad'})

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")
stcity=input("Enter City:")

getdata({'id':stid,'name':stnm,'sub':stsub,'city':stcity})
