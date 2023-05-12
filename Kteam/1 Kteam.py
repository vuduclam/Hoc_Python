#########***********************************************************************************************
#Tên biến không được trùng với 1 số từ khóa trong python

#########***********************************************************************************************
#a= 4                       #kiểu integer
#a= 9.6                      #kiểu float
#a='hj'                     # string có thể dấu ngoặc đơn hoặc ngoặc kép
#tuoi, doi = 17, 'hung hon'            #khai báo nhiều biến
#a='hj'
#print (tuoi)
#print (type(doi))
#from decimal import*
#getcontext().prec=30                        # tổng số nguyên và thập phân là 30 chữ số
#d= Decimal (10) / Decimal (3)                       #Lưu ý: viết hoa Decimal, kiểu dữ liệu decimal.Decimal
#print(d)
#from fractions import Fraction #phân số
#d= Fraction (1,5)
#e= Fraction (3,4)
#print (d + e)
#d= complex (2,5)                          #số phức
#print (d.real)                         #lấy phần thực
#print (d.imag)                                #lấy phần ảo
#a= 7/3                               #là số thực
#a= 7//3                          #lấy phần nguyên
#a= 7%3                           #lấy phần dư
#a= 7**2                           #lũy thừa 7 cơ số 2
#print (a)
#import math                        #thư viện công thức toán học  
#a= math.trunc(5.0123123123)
#print (a)
#a=+=5, -=5, *=5, 

#########***********************************************************************************************
# "aa", 'aa', '''aa''',"""aa""" là chuỗi

#d="""how
#kteam"""                                     #chuỗi nhiểu dòng phải dùng ''' ''' hoặc """ """
#print (d)

#print ('toi la \nminh')                              #\n là dấu enter

#print (r'toi la \nban mon biet \nssss')              #có r vào chuỗi thì \n sẽ không còn tác dụng

#a= 'lamlamgi\n'
#b=a*5 #sẽ nhân chuỗi lên
#print(b)

#a= 'lamlamgi' ;                        #b='A'
#c=  b in a                             #b có nằm trong a thì true

#c1= a  + 'để hùng' + b ;               #cộng chuỗi

#d= a[1] #vị trí trong chuỗi
#e = a[-2]
#f= len(a)
#g=a [1:None] 
#g=a [1:None:2]                         #bước nhảy 2 cứ 2 chữ cái sẽ lấy 1 chữ
#print (d); #print (d); print (e);
#print (g); #print (g)
#aa= int ("89") +5                  #gán lại kiểu thì phải đúng kiểu nếu từ string
#aa= float('89')
#bb= int (6.7)                          #lấy phần nguyên
#cc= str (69.5) + "5"
#print (cc)
#print (type(cc))
#a="how"
#a=a[None:1] + "0" + a[2:None]
#print(hash(a))

#########*******************************************************************************************
#a= "are you"
#print (hash(a))
#b = 'my team is %s' %("2.9")                    #gán string thì số có thể có dấu ngoặc đơn hay kép
#a1 = 'my team is %s %s' %('hinh','vuong')
#b = 'my team is %s' %('2.9')                    #gán string thì số có thể có dấu ngoặc đơn hay kép
#c = 'my team is %s' %("aa")
#d = 'my team is %d' %(3.5)                         #chỉ được gán số và kết quả sẽ ra số nguyên
#print (d), #print (b), #print (c)
#d="%s" %('1')
#e="%.1f" %(1.44)                          #bắt buộc không có dấu ngoặc đơn hay kép, 1 là lấy sau dấu phẩy 1 chữ số
#print (e), #print (e)

#########***************************************************************************** định dạng string f
#hh= f'aaaa' # đơn hoặc kép
#print (hh)
#ee= 'this is {lam}'                  #in ra sẽ có dấu ngoặc nhọn
#name ='hoang'
#name1='linh'
#bb= f'{{name}} la ai, {name1} la nguoi'               #thêm dấu ngoặc nhọn sẽ vẫn là biến
#print (bb), #print (ee)

##########************************************************************************** format
#r='1: {1}, 2: {0}'.format(111,222)                       # 111 là ở vị trí 0
#r1='1: {one}, 2: {two}'.format(one=111, two =222)
#r2='1: {}, 2: {}'.format(333,444)
#r3='1:%d, 2:%d, 3:%d'%(1.67,2.562,3.52)  # %d là chỉ lấy số nguyên
#r3='lam{:*^12}lam'.format('') # ^ là căn giữa, > là lề trái, < là lề phải, *là kí tự ta sẽ tự cho để thêm vào chỗ trống
#r4='vu{:<12}lam'.format('duc')
#r4='+ {:-^6} + {:-^12} + {:-^6} +'.format('','','')
#print (r), #print (r1), print (r2), print (r3), print (r4)

#############*************************************************************************
#a='atCó gì hóta'
#a1=a.capitalize()                      #viết hoa chữ cái đầu tiên
#a2=a.upper()                         #viết hoa hết
#a3=a.swapcase()                       # thường thành hoa, hoa thành thường
#a4=a.title()                           #chữ cái đầu tiên của mỗi chữ sẽ thành hoa
#a5=a.center(30,'*')                     #canh giữa or center(30)
#a6=a.rjust(20,'*')                         #canh trái
#a7=a.encode()
#a8=a.join(['a','b','  c'])                  # cộng chuỗi (ngoăc tròn hoặc vuông)
#a9=a.replace('ó','L',2)                         #số lượng thay 2 chữ ó
#a10=a.strip('at')                                 #cắt khoảng trắng hai đầu và kí tự được đề cập ----lstrip, rstrip.
#a2=a.lower()                                #viết thường hết
#print(a8),print(a9)
#print(a2)

#############******************************************************************************************
#a='vu duc lam'
#b=a.split('u')                     #cắt các chữ u (kết quả trả sẽ nằm trong dấu ngoặc vuông-kiểu list)
#a2=a.split(' ',1)                  #cắt số lượng 1 khoảng trắng  (kết quả trả sẽ nằm trong dấu ngoặc vuông-kiểu list)
#a3=a.rsplit(' ',1)                     #cắt số lượng 1 khoảng trắng từ bên phải
#a4=a.split('u')                            #cắt các chữ u
#a5=a.rpartition('u')                        #cắt tại chữ u thành 3 phần tử (kết quả trả sẽ nằm trong dấu ngoặc tròn-kiểu tuple)
#a6=a.partition('y')                   #nếu không có chữ y thì sẽ tạo ra 3 phần tử với 2 phần tử là khoảng trắng
#a7=a.count('u')                           #tìm số lượng chữ u
#a8=a.count('u',1,5)                    #tìm số lượng chữ u trong dải 0 tới 4 của chuỗi
#a9=a.startswith('v')                         #có bắt đầu bằng chữ v hay không (kết quả trả về True-False)
#a10=a.startswith('v',0)             #có bắt đầu bằng chữ v hay không (bắt đầu từ vị trí  0)
#a11=a.endswith('c',0,5)
#a12=a.find('u')                       #chuỗi hay chữ bắt đầu từ số bao nhiêu, nếu tìm không ra sẽ báo -1
#a13=a.rfind('b')                      #từ bên phải qua thì chuỗi hay chữ bắt đầu từ số bao nhiêu, nếu tìm không ra sẽ báo -1
#a14=a.index('v')                         #chuỗi hay chữ bắt đầu từ số bao nhiêu, nếu tìm không ra sẽ báo lỗi
#a15=a.islower()                  #chuỗi viết thường sẽ true, 1 chữ cái hoa sẽ false
#a16=a.isupper()                     #chuỗi viết hoa sẽ true, 1 chữ cái thường sẽ false
#a17=a.isdigit()                      #chuỗi là số sẽ true '31313', chữ sẽ false '1231dsad'
#a18=a.isspace()                       #chuỗi là khoảng trắng sẽ true ' ', chữ sẽ false ''
#print (b)
#print (a8)
#print (a15)

#############******************************************************************List (có thể chứa chính nó và những cái khác)
#a=[[1,2,3],[7,'lam']]
#b=(i for i in range(3))                 #in list ra bắt đầu từ 0 (kết quả trả về [0,1,2])
#c=list(b)                                 #nếu ngoặc tròn ở b trên (comprehension) thì phải có list(b) để phân biệt tuple(b), ngoặc vuông thì không cần
#b=[i for i in range(3)]                           #ngoặc vuông thì không cần list(b)
#print(a)
#c=[[i,i*2] for i in range(1,3)]
#d=list('kteam') #hoặc d=list ([1,2,3]) hoặc ((1,2,3))

#********************************************************************toán tử list gần giống chuỗi
#e=[1,2]
#e+=['one','two']                         # viết tắt của e=e+['one','two'] và list cộng list, chuỗi cộng list sẽ báo lỗi
#e*=2                 #nhân list với 1 số, không nhân list với list được
#b= 1 in e                              #kiểm tra 1 có nằm trong list không, kết quả True-False
#a=[1,2,'a','b',[3,4]]
#b=len(a)                            #độ dài của list
#b=a[0]                          #lấy phần tử tại vị trí 0 của list
#b=a[1:3]                             #lấy phần tử trong dải 1 tới 3 (a[1:]; a[:3]; a[::]; a[::-1])
#b=a[::2]                         #lấy phần tử cứ bước nhảy 2 thì lấy 1 chữ số
#b1=a[4][1]                           #lấy phần tử tại vị trí 4 và lấy phần tử vị trí 1 của list vừa lấy ra
#print(e)

#********************************************************************thay đổi phần tử trong list
#a=[1,2,'a','b',[3,4]]
#a[1]= 'kteam'                #muốn thay đổi phần tử trong list thì gọi ra và gán 1 tên khác
#a=[1,3,4] #*
#b=a                                #nếu gán list với list thì khi thay đổi giá trị b, giá trị a sẽ chạy đồng thời.
#b=list(a)
#print(a)                        #nên là b=list(a) hoặc b =a.copy() sẽ không thay đổi a khi thay b.
#print(b)
#b[0]='kteam'                         #nếu thay đổi giá trị trong list con thì giá trị cũng sẽ chạy theo (a=[[1,2,3],[4,5,6] ///b[0][0]='kteam')
#print(a)
#print(b) #*

#*****************************************************************************************đếm số lượng phần tử trong list
a=[1,2,3,4]
#b=a.count(1)                   #đếm số lượng phần tử 1 trong list 
#c=a.index(3)                     #vị trí của phần tử 3 trong list
#d=a.copy()                    #a không thay đổi khi thay đổi d
#a.clear()                       #kết quả c ra None và a ra []
#print(a)
#tien=[34,45] #*
#gau=tien
#print(tien)
#print(gau)
#gau=[]                        #vì đã gán qua list khác nên sẽ ra 2 kết quả khác nhau
#gau.clear()                                  #sẽ cùng []
#print(tien)
#print(gau) #*
#a=[1,9,2,3,9]
#a.append([4,5,[6,7]])               #sẽ thêm phần tử 4 hoặc [4,5] vào list trên  (nhưng tuple không có phương thức này mà chỉ có a+= )
#a.extend([4,5,[6,7]])                          #sẽ thêm từng phần tử 4,5 vào list trên ở cuối
#a.insert(1,9)                      #sẽ thêm phần từ 9 vào vị trí thứ 1
#a.pop(0)                        #bỏ đi vị trí thứ 1 và nếu pop() thì tự động bỏ đi phần tử cuối cùng
#a.remove(9)                 #bỏ đi phần tử 9 đầu tiên trong tất cả các số 9 trong list
#del a[2]                    #bỏ đi vị trí thứ 2 trong list
#a.reverse()                              #đảo chiều list
#a.sort()                            #tự động sắp xếp theo chiều tăng dần
#a.sort(key = None, reverse = True)                   #True sẽ sắp xếp giảm dần, False sẽ sắp xếp tăng dần
#print(a)

#############*********************************************************************Tuple (có thể chứa nó và những cái khác)
#a=(1,2,3)                            #kiểu dữ liệu Tuple 
#a=(1.5)                        #sẽ hiểu là kiểu dữ liệu int
#a=tuple([1,2])                       #hoặc tuple((1,2,3))
#a=(i for i in range (3) if i % 2 == 0)

#b=tuple(a)                         #phải có tuple(a) để ra kết quả
#print(a)
#*****toán tử tuple giống chuỗi
#a=(1,2,[1,2])
#b= a + ('one','two')
#a*=2                           #nhân tuple với 1 số, không nhân tuple với tuple được
#b= 1 in a                                #kiểm tra 1 có nằm trong tuple không, kết quả True-False
#b=a[0]                         #lấy phần tử tại vị trí 0 của tuple
#b=len(a)                          #độ dài của tuple
#b=a[-1]                   #lấy phần tử cuối cùng của tuple
#*****đếm số lượng phần tử trong tupple
#b=a.count(2)                              #đếm số lượng phần tử 1 trong tuple 
#c=a.index(2)                #vị trí của phần tử 2 trong tuple
#print(b)
#*****không thay đổi được phần tử trong tuple như list được

