###########************************** Hashable: không thay đổi được giá trị tuple(), chuỗi (chiếm ít dung lượng hơn vì nó sẽ cuốn gói sang chỗ khác)
# Unhashable: thay đổi giá trị được như list[], dict
#a=[1,2]
#b=[3,4]
#print(id(a))
#print(id(b))
#a=a+[6]
#b+=[6]
#print(id(a))
#print(id(b)) #kết quả giống nhau
a=(1,2)
print(id(a))
a+=(3,4)
print(id(a))

#set chỉ chứa hashable object (tuple và chuỗi), không chứa được nó và list vì set và list không phải hashable object
#a={1,(3,4),1,2}  #nó chỉ chứa phần tử 1 lần nếu phần tử đó có nhiều lần xuất hiện
#print(a)
#b={}  
#print(type(b)) # cái này thuộc dict 
#c={i for i in range (3)}
#print(c)
#a=set((1,1,5,7,8,3)) #hoặc set([1,2,3])
#print(a)
#a=set() #kết quả ra set()-là thuộc set
#*****toán tử trong set
#print(1 in {1,2,3}) #True vì có 1 trong set
#print({1,2} in {1,2,3}) #False vì không có {1,2}
#print({1,2,3,4}-{2}) #trừ set nếu set lớn trừ set nhỏ
#print({1,2}-{1,2,3,4}) # kết quả ra set() vì nhỏ không trừ lớn
#print({1,2,3}&{1,3,4,5}) #phần tử chung
#print({1,2,3}|{2,3,4}) #kết hợp
#print({1,2,3}^{2,3,4} #lấy phần tử không chung
#a={4,2,3}
#a.clear() # kết quả ra set()
#print(a)
#a.pop() #bỏ phần tử đầu tiên
#a.remove(3) #bỏ phần tử 3 trong set, nếu không có số đó sẽ báo lỗi
#a.discard(5) #bỏ phần tử 3 trong set, nếu không có số đó sẽ không báo lỗi và vẫn là set đó
#b=a.copy()
#a.add((2,5)) #nếu có phần tử đó rồi thì vẫn là set đó
#print(a)
#a={1,2} #*
#print(id(a))
#a.add(4)
#print(id(a)) #*sẽ vẫn chung id

#############***************************Dict (key:value) 
#a={'name':'kteam','member':69}
#print(a)
#a={} #sẽ ra {}
#***a=dict(K='kteam',hk='howkteam')
#***b=('name','kteam'),('member',69)
#a=dict(b) #sẽ tạo cặp key:value như trên
#***iter=('name','kteam')
#a=dict.fromkeys(iter) #sẽ tạo 2 key như trên nhưng value là None
#a=dict.fromkeys(iter,'m') #sẽ tạo 2 key như trên nhưng value là m
#print(a['name']) #lấy value từ key
#a['name']="man" #thay value của key
#a['lam']="vu" #nếu key đó không có trong danh sách thì sẽ tự động nhập vào
#print(a)

#############***************************Dict
#a={'name':'kteam',(1,2):69}
#print(a)
#b=a.copy() #sẽ tạo ra vùng nhớ mới cho b
#print(b)
#b=a.clear()
#b=a.get('name') #lấy value của key, nếu không có key đó thì kq ra none
#b=a.get('minh','free') #nếu key không có thì sẽ ra value 'free' đã tạo
#b=a.items() #sẽ ra dict_items([('name', 'kteam'), ((1, 2), 69)])
#c=list(b) 
#print(c[0]) #lấy giá trị trong list
#b=a.keys() #lấy ra danh sách key
#b=a.values() #lấy ra danh sách value
#b=a.pop('name') #lấy ra value thuộc key đó thì khi in lại sẽ bỏ key:value đó
#b=a.popitem() #lấy ra value bất kì
#b=a.setdefault('m','nn') #có key thì ra value, không có thì ra none
#a.update(k='tea',g='sa') #thêm các key:value
#print(a)