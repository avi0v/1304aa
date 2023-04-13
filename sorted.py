a={2:'avi',1:'sajan'}
print(sorted(a))
b=sorted(a.keys())
print(b)
b=sorted(a.values())
print(b)
b=sorted(a.items(),key=lambda x:x[0])
print(b)
b=sorted(a.items(),key=lambda x:x[0],reverse=True)
print(b)

#del 
# del(key) - del key as well as values too
# same dict.pop(key)