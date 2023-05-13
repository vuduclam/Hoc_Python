# a = [1,2,[6,7]]
# print(id(a))
# a+=[3,4]
# print(id(a))
# a=(1,2) #*
# print(id(a))
# b=a
# a+=(3,4)
# b = a.copy()
# b=tuple(a)
# b[2][0] = 4
# c=b.clear()
# print(a)
# print(b)
# print(c)
# print(dir(tuple))
# print(id(a))
# print(id(b))
# a=[(1,2),(5,6)]

# print(a)
# b=a[0]
# print(type(b))
a=[[1,2]]
b=sum(a,[2])
print(b)