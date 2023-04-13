#creating set
# s={1,2,3,4}
s={1,2,4,'dfsd',5,6,7,8,9,1,'ww'}
# no duplicate allowed 
# auto del and when ever set called - random arrangement 
# set donot maintain the order
print(s)

s=list(s)
print(s)
s=set(s)
print(s)
print('see no order maintained')
# sets are mutable
s.add('ffffffffff')
print(s)
#remove
s.remove(5)
print(s)
s.discard('ww')
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)