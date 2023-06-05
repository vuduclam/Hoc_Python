#*************************************************************************************Cách cài thư viện
# Tạo môi trường ảo



# ******************************************************************************************Toán tử
# >=, <=, >, <, ==, !=, and, or, not sẽ ra giá trị True, False
# Falsy bao gồm '', None. 0, 0j
# print(1>2)                            #sẽ ra False
# print(0 and 2)                        #vế đầu true sẽ trả giá trị thứ 2
# print(3>1 or 2)                       #vế đầu false sẽ trả giá trị thứ 2
# age=34
# print(f'i am {age}')                  #f là địng dạng string, type là string
# print('i am', age)                    #type là tuple
# print('i am ' + str(age))             #type là str
# print('i am {}'.format(age))          #type là str
# username = input ('hay nhap:')
# usd= input('hay nhap: ')              #input sẽ trả về string
# usd= float(input('hay nhap: '))
# print(usd*5)
# a = 8
# b=('i am' + str(a))                   #b là str
# b = ('i am', a)                       #b là tuple
# print(type(b))
# print(ord('a'))                       #hàm lấy mã ascii
# print(chr(97))                        #hàm từ mã ascii ra 

#***************************************************************************List
#    0 1 2 3                            #thứ tự của list
# -4,-3,-2,-1                           #thứ tự của list
# a=[1,2,3,4.5]
# dir(list)                              #sẽ ra các hàm thuộc list
# print(dir(list))
# del a[2]                               #xóa phần tử thứ 2 trong list
# print(a)
# b=max(a)                               #chỉ đúng với số, sẽ lỗi nếu list chứa str và int, lỗi với list trống
# b=min(a)                               #sẽ lỗi nếu list chứa str và int
# print(b)

#***************************************************************************List
# from pprint import pprint              #pprint sẽ in ra xuống dòng nếu list đó dài
# a=[1,2,3]
# b=a     
# print(a,b)                              
# print (b is a)                         #True
# b=a.copy()
# print (b is a)                         #False khi dùng copy vì b và a nằm trên 2 bộ nhớ khác nhau
# print(id(a),id(b))                     #hàm id kiểm tra vị trí bộ nhớ, giống nhau nếu b=a, khác nhau nếu copy
# b=a[start:stop;step]                   #lấy ra list mới 

# from copy import deepcopy                # b thay đổi nhưng a không đổi
# a=[1,2,[3,5]]
# b=deepcopy(a)
# b[2][0]=4
# print(a)
# print(b)
# print(id(a))
# print(id(b))

#***************************************************************************list sang chuỗi
# a=['a','2','3']                               #join cho chuỗi
# b=''.join(a)                                  #list thành chuỗi, thì list phải chứa chuỗi hết
# a=['a',2,3]      
# b='---'.join(map(str,a))                       #nếu list có số, phải convert sang chuỗi bằng map
# print(b)                                       #'' có thể thêm vào 



#***************************************************************************Set
# Check những dòng trùng
# help(set.pop)                          #Kiểm tra cách dùng hàm 

# print(isinstance(1,int)                #Kiểm tra True or False
# print(ord('a') ^ ord('b'))               #XOR    1 so 1 ra 0, 0 so 0 ra 0, 0 so 1 ra 1 
# print(abs(0j))                           #số, True, False, số phức (Căn bậc hai a^2+b^2)       
# print('a')                               #kết quả ra a
# print(repr('a'))                         #kết quả ra 'a'-str

# a="a"
# b=4
# print(f'{a!r}')                          #kết quả ra 'a'
# print(f'{b!r}')                          #kết quả ra 4

#***************************************************************************Nâng cao Set
# a={1,2,3}
# b={2,3,4}
# c={3,5,6}
# c=a.intersection(b)                        #tìm phần tử chung--b có thể là list, tuple, dict và kết quả là set
# c=a & b                                    #tìm phần tử chung--cả a và b phải cùng là set
# c=a.difference(b)                          #ra phần tử nằm trong a, không b--b có thể là list, tuple, dict và kết quả là set
# c=a - b                                    #ra phần tử nằm trong a, không b--cả a và b phải cùng là set
# c= a.union(b)                              #tập hợp phần tử a và b--b có thể là list, tuple, dict và kết quả là set
# c=a|b                                      #tập hợp phần tử a và b--cả a và b phải cùng là set
# d=a.symmetric_difference(b)                #tập hợp nhưng bỏ phần chung
# d=a ^ b                                    #tập hợp nhưng bỏ phần chung

# d=a.intersection(b).intersection(c)        #nhiều set
# d=a.difference(b).difference(c)
# d=a.union(b).union(c)

# a={'name':'kteam','age':69}             
# b=a['age']                                   #lấy giá trị value từ key, key khác sẽ báo lỗi
# b=a.get('ae')                                #lấy giá trị value từ key, key khác sẽ ra None
# b=a.get('ae',98)                             #lấy giá trị value từ key, nếu key khác ta tạo value ngay trong lệnh
# print(a)
# print(type(b))



# a=[1,2,3]
# b=sum(a)                                  #cộng các giá trị trong list đơn bắt đầu từ 0
# b=sum(a,2)                                #cộng các giá trị trong list đơn bắt đầu từ 2 
# b=sum(a,[2,3])                            #sẽ tạo ra list đơn khác
# print(b)

#***************************************************************************If-elif-else
# n=int(input("nhap so n: "))
""" if n>0:
    print("duong")
elif n<0:
    print("am")
else:
    print("0") """
# print("duong" if n>0 else "am")                     #cú pháp ngắn gọn if else--không nên sử dụng
""" a, b = map(int,input().split('0'))
print(a if a<b else b) """

# a=input('nhap so nguyen: ').split()                 #input().split(): ra list chứa string
# print(a)

# a, b=map(int,input().split())                      #nhập số theo 1 hàng
#                                                    #map có hàm sẵn sẽ nhanh hơn list comprehension, ngược lại map hàm tự định nghĩa lâu hơn
                                                      
# print(a)
# a=4
# print(eval('1+2+2.5'))                               #hàm đánh giá biểu thức nằm trong chuỗi
# print(eval('a+2+2.5')) 
# a,b=map(eval,input().split())                        #để có thể nhập số nguyên và thực
# print(a)

# a=[1,2,3,'a']
# print(*a)                                                 #sẽ phá list in ra 1 2 3 4
# print(*a,sep="")                                       #sẽ phá list in ra 1$2$3$4  

# x=2.4567                                                  #làm tròn 2 chữ số sau thập phân--str
# print(format(x,".2f"))

# x=2.456                                                 
# print(round(x))                                         #làm tròn chữ số trước thập phân--int
# x=2.456                                                 
# print(round(x,2))                                       #làm tròn 2 chữ số sau thập phân--int
# print(pow(2,3))                                         #lũy thừa 2^3--int

# a,b=[2,3]                                               #tuple hoặc list in ra a=2--int                                          
# print(type(a))

#***************************************************************************vòng lặp
""" for i in range(3):
    print (i)  """                                       #list(range(3)) chỉ từ 1 tới 2

""" for i in range(3):
    if i & 2 == 0:
        print(i, end= ' ') """

""" for i in range(4):                                         
    print (i, end=' ')  """                                 #thêm end sẽ in ngang, còn không sẽ in dọc 

""" b=[i for i in range(3)]                                 #b sẽ ra list
b=(i for i in range(3))                                     #phải có lệnh list(b)
print(list(b)) """

""" s=input('nhập: ')
while s != 'q':
    print('hello')                                            #sẽ in hello vô tận
    s=input('nhập: ')  """                                       

#break: thoát hoàn toàn ra khỏi vòng lặp chứa nó
#continue: bỏ qua các câu lệnh bên dưới nó và chuyển sang vòng lặp mới
""" for i in range (10):
    if i>5:
        break                                        
    print(i, end=' ') """

""" for i in range (20):
    if i > 10:
        continue                                        
    print(i, end=' ') """

""" for i in range (10001):  ***********                                #for chạy hết sẽ in ra tới 20 rồi tới else 'success'
    print(i, end=' ')
else:
    print('success')  """

""" for _ in range (20):   
    print('hello') """

#đếm số lượng số nguyên tố
""" a=0
for i in range(1,102):
    if i == 1:
        continue                                                 #đúng thì chạy lên vòng lặp
    for n in range(1,int(i/2+2)):
        if i == 2:
            a+=1
            break
        else:
            if n != 1 and i % n == 0:
                break
    else:
        a+=1
print(a) """

#tính tổng của 1 số n
""" n = 1234                                                  
b = 0
while n > 0:
    a=n % 10
    b += a
    n //= 10
print(b) """

# print(list(range(2,2)))                                #ra list rỗng
# print(int(3**0.5)+1)

#***************************************************************************List, set, dict comprehension
""" a = {85,52,3,4}                                      #list, tuple, dict
for i in a:
    print(i) """

""" a={'ten': 'lam',
   'tuoi': 23,
   'gender': 'male'} """

""" for i in a:                                             
    print(i)  """                                            #in ra key

""" for i in a.values():    
    print(i)  """                                            #in ra values

""" for i in a.items():
    print(i)   """                                           #in ra tuple (key, values)

""" for i in a.items():
    c,d=i
    print(c)
    print(d)
    print('-'*20) """

#List comprehension (tạo ra cái mới)
""" a=[45,5,65,32]                                     #cách dài
b=[]
for i in a:
    y=i*2
    b.append(y)
print(i)                                               #có thể in ra i=cuối
print(b) """

""" a=[45,5,65,32]                                     #cách ngắn: List comprehension
b= [i*2 for i in a]
print(i)                                               #in ra i bị lỗi
print(b) """

#Set comprehension (tạo ra cái mới)
""" a={'k','j'}                                           #in hoa trong set
s={i.upper() for i in a}
print(s) """

#Dict comprehension (tạo ra cái mới)
""" a={6: 2,
   5: 23,
   10: 5}
b={i*2: y for i,y in a.items()}
print(b) """

#Zip phải có list(), tuple()
""" a=(2,3,5)                                      #list, tuple cũng sẽ kết hợp được
b=('a','f')
print(list(zip(a,b)))                              #in ra list tuple, tuple tuple không có 5
print(dict(zip(a,b))) """                          #in ra dict

#enumerate 
""" a=(2,3,5)
print(list(enumerate(a)))                             #sẽ tạo ra list tuple kết hợp chỉ số thứ tự với list 
print(list(enumerate(a,start=2))) """                  #sẽ tạo ra list tuple kết hợp chỉ số thứ tự với list bắt đầu từ 2

# a=(2,3,5,48,97)
# # b=[i for i in a if i%2!=0]                  
# # print(sum(b))                                         #tính tổng các số lẻ trong list
# c=0

# a=(2,3,5,48,97)
# b=[i*2 if i %2==0 else i*3 for i in a]
# print(b)                                                #in ra list số chẵn nhân 2. số lẻ nhân 3


# a=(2,3,5,48,97)                                           #in ra index - list
# for b,c in enumerate(a):
#     print(f'{b} - {c}')

# a=(2,3,5,48,97)                                           #in ra index lẻ- list
# for b,c in enumerate(a):
#     if b %2!=0:
#         print(b,c)

# a=[[2,3],[5,48]]   #or a = [(2,3),(5,48)] 
# b=dict(a)
# print(b)

#***************************************************************************Hàm (tái sử dụng lại code, gom lại các code lặp lại)
""" def my():                                              #định nghĩa hàm
    print("hello")
my() """                                                   #phải gọi hàm ra 

""" def my(a , b):                                         #để biến ở trong hàm, gọi hàm thì phải truyền vào giá trị
    print(f'{a} {b}')
my('asad','ass')   """                                     


""" def my(a , b):
    print(f'{a} {b}')
my('asad','ass',1)   """                                #bị lỗi vì gọi hàm có 3 đối số

""" def my(a , b = 'kk'):                              
    print(f'{a} {b}')
my('asad')     """                                      #b đã có rồi, nên gọi hàm có a
# my(b='jkjk',a='asad')                                 #hoặc gán lại b,a

""" def my(a,b='kk'):                                   #return trả về giá trị và các câu lệnh sau nó dừng
    return (f'{a} {b}')                                 
c= my('asad')                                           #phải gán biến c cho hàm để có thể in ra
print (c) """

""" def my(a,b):                                     
    return (a+b)                                                                      
print(my(5,6))  """                                     #không tạo biến thì in ra lun 

""" def my(a,b='kk'):  
    if a:                                               #nếu có a (False. True)
        return (f'{a} {b}')                             
    return (f'Kenny {b}')                               #không cần else   
c= my('asad')                                           #vì asad là True nên đúng return trên, có thể gán tên tại vị trí gọi hàm
print (c) """
                                         
""" def my(a=[]):                                       #nếu là list, lúc gọi hàm sẽ bị thay đổi giá trị khi gọi lại
    a.append(2)
    print(a)
my()                                                    #ra [2]
my() """                                                #ra [2,2]

""" a=[52,6]
def my():
    b=a+[1,3]
    print(b)
my()    """ 

# print((lambda x,y:x+y)(1,2))
""" a=lambda x,y:x+y                                     #số thì ra tổng 1,2 ra 3
print(a('1','2')) """                                    #string thì ghép lại 12

#Class function
""" def greet(a):
    print('hello ' + a)                                  #giá trị trong hàm luôn trả về None, không có return cũng được
b=greet                                                  #gán biến cho hàm
print(b("Jen")) """                                      #thay vì gọi hàm, ta gọi biến, print cái này sẽ ra None 

""" def greet(a):
    pass   """                                           #trong hàm không được để trống, dùng pass để thay thế

""" def greet(x,y,z):
    return x+y+z
print(greet(1,2,3)) """

""" def greet(*args):                                       #*args tập hợp lại các biến (đối số vị trí)
    print(type(args))                                       #args sẽ ra tuple  
    return sum(args)
print(greet(1,2,3)) """

""" a=[1,50,3,4,8]
first, *mid, last = a
print(first)                                               #in ra số đầu
print(mid)                                                 #in ra list giữa
print(last)  """                                           #in ra số cuối

""" def add(*list, a):
    return(a(list))
print(add(1,2,3,a=sum)) """           

#Lưu ý (Không nên in list với số)
""" a=[[]] * 5                                             #sẽ ra [[2],[2],[2],[2],[2]]
a[1].append(2)                                             #không thể tạo ra [[],[2],[],[],[]]
print(a) """

""" a=[[2] for i in range (5)]                                 #muốn thay thế phần tử trong list thì dùng for                     
a[1].append(5)
print(a) """