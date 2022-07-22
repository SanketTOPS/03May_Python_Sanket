myset={'A','B','C','D','E','F'}

#print(myset)

#print(len(myset))

"""for i in myset:
    print(i)"""

print(myset)

myset.add("G")
myset.update(["H","I","J"])
#myset.remove("G")
#myset.pop()
#myset.clear()
#print(myset)


newset={"P","Q","R","S","A","B"}

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)
