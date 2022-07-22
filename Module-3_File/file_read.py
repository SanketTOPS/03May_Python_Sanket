fl=open("stdata.txt","r")

#print(fl.read())
#print(fl.readline())
#print(fl.readlines()[2])

"""n=0
for i in fl:
    #print(i)
    print(f"Line={n} : {i}")
    n+=1"""

ln=fl.readline()

while ln != "":
    print(ln)
    ln=fl.readline()


