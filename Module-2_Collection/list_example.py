from hashlib import new


tech=["Python","Android","JAVA","PHP","iOS"]

"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[0:3])
print(tech[3:])
print(tech[:4])
"""
#print(len(tech))

"""for i in tech:
    print(f"{i} = {len(i)}")
"""

#print(tech)
"""tech[2]="Angular"
print(tech)"""

"""for i in tech:
    print(i)"""

# Index[0]=Python 
# Index[1]=Android

#print(tech.index('PHP'))

"""for i in tech:
    print(f"Index[{tech.index(i)}]={i}")"""


"""n=0
for i in tech:
    print(f"Index[{n}]={i}")
    n+=1"""

"""i=0
while i<len(tech):
    print(tech[i])
    i+=1"""

#[print(i) for i in tech]


"""if "Python" in tech:
    print("Yes...")
else:
    print("Noo")"""

# ------------------------------------------------------ #

print(tech)
tech.append("React")
tech.insert(2,'Angular')
#tech.remove('PHP')
#tech.pop()
#tech.pop(3)
#tech.clear()
#del tech[1]
#del tech

#tech.reverse()
#tech.sort()
#print(tech)

#newlist=tech.copy()
#print(newlist)

newlist=["C","C++","C#","DS"]
#print(tech+newlist)
tech.extend(newlist)
print(tech)


