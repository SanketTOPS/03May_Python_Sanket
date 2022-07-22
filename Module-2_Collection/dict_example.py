mydict={'id':1,'name':'sanket','city':'rajkot'}

"""print(mydict)
print(mydict.get('name'))
print(mydict['city'])

print(mydict.keys())
print(mydict.values())

print(len(mydict))
"""

"""if 'name' in mydict:
    print('Yes...')
else:
    print('Noo...')
"""

"""if 'rajkot' in mydict.values():
    print("Yes...")
else:
    print("Noo")"""

#print(mydict)
#mydict['id']=2
mydict['sub']='python'
#print(mydict)

# ------------------------------------------ #

"""for i in mydict:
    print(i)
"""

"""for i in mydict.values():
    print(i)"""

"""for i in mydict.items():
    print(i)"""


# Key=id and Value=1
# Key=name and Value=sanket

"""for i,j in mydict.items():
    print(f"Key={i} and Value={j}")"""

print(mydict)
#mydict.pop('name')
#del mydict
#print(mydict)

newdict=mydict.copy()
print(newdict)