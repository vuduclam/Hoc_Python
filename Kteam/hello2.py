###########************************** Hashable: không thay đổi được giá trị tuple(), chuỗi (chiếm ít dung lượng hơn vì nó sẽ cuốn gói sang chỗ khác)
# Unhashable: thay đổi giá trị được như list[], dict

#set chỉ chứa hashable object (tuple và chuỗi), không chứa được nó và list vì set và list là  unhashable object
# a={1,(3,4),1,2}                               #nó chỉ chứa phần tử 1 lần nếu phần tử đó có nhiều lần xuất hiện
# print(a)
# b={}***************                           #set rỗng sẽ thuộc dict
# print(type(b))                                 
# c={i for i in range (3)}
# print(c)
# a=set((1,1,5,7,8,3)) #hoặc ***********
# set([1,2,3])
# print(a)
# a=set()                                       #kết quả ra set()-là thuộc set
#*********************************************************************************toán tử trong set
# print(1 in {1,2,3})                          #True vì có 1 trong set
# print({1,2} in {1,2,3})                      #False vì không có {1,2}
# print({1,2,3,4}-{2})                         #trừ set nếu set lớn trừ set nhỏ
# print({1,2}-{1,2,3,4})                       #kết quả ra set() vì nhỏ không trừ lớn
# print({1,2,3}&{1,3,4,5})                     #phần tử chung
# print({1,2,3}|{2,3,4})                       #kết hợp
# print({1,2,3}^{2,3,4}                        #lấy phần tử không chung
# a={5,6,2,8}
# a.clear()                           #kết quả ra set()
# print(a)
# a.pop()                             #bỏ phần tử bất kì
# a.remove(3)                         #bỏ phần tử 3 trong set, nếu không có số đó sẽ báo lỗi
# a.discard(3)                        #bỏ phần tử 3 trong set, nếu không có số đó sẽ không báo lỗi và vẫn là set đó
# b=set(a)                            #khác bộ nhớ
# b=copy(a)                           #Khác bộ nhớ
# b=a                                 #Cùng bộ nhớ
# b.clear()                           #ra set()
# a.add(2,5)                          #nếu có phần tử đó rồi thì vẫn là set đó
# a.update((1,(5,6),6))  #hoặc
# a.update(['a',1.5,(2,3),4])         #mỗi lần enter thứ tự sẽ khác nhau, nhưng số nguyên theo thứ tự tăng dần                 
# print(a)
# a={1,2} #*
# print(a)
# print(id(a))
# a.add(4)
# print(b)
# print(id(b))  
# print(c)                       

#############***************************************************************************Dict (key:value) 
# a={'name':'kteam','age':69,'aaa':'awdf'}                 #các key không được trùng nhau, nếu trùng nhau nó sẽ lọc từ đầu tới cuối
# # print(a)

# import json                                  #để in theo hàng lối thì import json và in ra sẽ là dấu nháy kép
# a={
#     'name':'kteam',
#     'age':69}                 
# print(json.dumps(a, indent=4))               #indent là thụt lề

# a={}                                          #sẽ ra {}

# a=dict(tr = 5,gh = 'howkteam')
# b=('name','kteam'),('member',69)
# a=dict(b)                                  #sẽ tạo cặp key:value như trên (bắt buộc b phải đủ)
# print(a)
# print(b)
# iter=('name','kteam')

# a=dict.fromkeys(iter)                       #sẽ tạo 2 key như trên nhưng value là None (không cần iter phải đủ)
# a=dict.fromkeys(iter,'m')                 #sẽ tạo 2 key như trên nhưng value là m
# print(a)

# print(a['age'])                             #lấy giá trị value từ key
# b=a.get('name')                             #lấy value của key, nếu không có key đó thì kq ra None
# b=a.get('minh','free')                      #sẽ ra value 'free' đã tạo nếu key không có 
# b=a.pop('name')                             #lấy giá trị value từ key  

# a['name']="man"                             #thay value của key
# a['lam']="vu"                               #nếu key đó không có trong danh sách thì sẽ tự động nhập vào cuối
# a.update(k='tea',g='sa')                    #thêm các key:value, các key sẽ tự động có dấu nháy str
# b={'id': 56, 'la' : 's'}                    #tạo dict mới rồi update
# b=[['as','sss'],['fgf','ưerw']]             #tạo tuple, list rồi update
# a.update(b)
# print(a)

#############***************************************************************************Dict
# a={'name':'lam','tuoi':27}
# print(a)
# b=a.copy() #sẽ tạo ra vùng nhớ mới cho b
# print(b)
# b=a.clear()

# b=a.pop('name')                    #bỏ key:value đó và lấy ra value thuộc key đó
# del a['name']                      #bỏ key:value đó       
# b=a.popitem()                      #bỏ key:value đó và lấy ra key:value thuộc tuple
# a.update(k='tea',g='sa')           #thêm các key:value, các key sẽ tự động có dấu nháy str

# b=a.keys()                         #sẽ ra dict_keys(['name', (1, 2)])
# b=list(a.keys())                   #tạo list các key, tuple(a) sẽ tạo tuple các key
# c=list(a)                          #tạo list các key, tuple(a) sẽ tạo tuple các key
 
# b=a.values()                       #sẽ ra dict_values(['kteam', 69])lấy ra danh sách value
# b=list(a.values())                 #tạo list các value, tuple(a) sẽ tạo tuple các value

# b=a.items()                        #sẽ ra dict_items([('name', 'kteam'), ((1, 2), 69)])
# b=list(a.items())                  #tạo ra list tuple [(key:value),(key:value)], tuple() thì ra tuple tuple((key:value),(key:value))

# print(a)
# print(c)
