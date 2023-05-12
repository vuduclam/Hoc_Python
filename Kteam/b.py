#############***************************Xử lý file
#a=open('lam.txt')
#b=a.read(3) # để trống sẽ đọc hết file, có số 3 thì sẽ đọc tới kí tự thứ 3
#b1=a.read() #sẽ đọc 3 kí tự tiếp theo 
#b=a.readline() #nếu có số sẽ đọc từng kí tự như read, để trống sẽ đọc hết dòng đó
#b1=a.readline()
#b=a.readlines() #sẽ đọc hết file và kết quả sẽ ra 1 list
#b1=a.readlines() #sẽ ra list [] vì b đã đọc hết file
#b=list(a) #sẽ thay thế readlines
#b=tuple(a)
#****a=open('lam.txt',mode='a+')
#b=a.write('thi mai') #sẽ thêm vào file
#a.close()
#print(b) 
#****a=open('lam.txt',mode='r')
#b=a.read() #đọc hết file thì con trỏ cuối file
#a.seek(0) #đưa con trỏ lại đầu file
#b1=a.read() #đọc tiếp file
#print(b) 
#print(b1)
#with open('lam.txt') as a:
 #b=a.read(2) #lưu ý trước b là space
#print(b) 
#print(b1)

#############***************************Iteration truy xuất từng phần tử
#a=[i for i in range (2)] #ngoặc vuông thì sẽ ra iterable
#print(a)
#a=(i for i in range (2))
#print(a) # sẽ ra <generator object <genexpr> at 0x0000021855892BA0> - iterator
#print(next(a))
#print(next(a))
#print(next(a)) #sẽ ra stopoteration vì hết phần tử
#a=(i for i in range (2))
#print(sum(a,-3)) #nếu dùng iterator thì sẽ không dùng được nữa
#print(next(a)) #sẽ ra stopoteration vì trên
#a=(i for i in range (2))
#print(max(a)) #sẽ ra giá trị lớn nhất
#print(max([],default='kteam')) #nếu rỗng thì sẽ ra giá trị default 
#a=(i for i in range (2))
#print(max(a)) #sẽ ra giá trị lớn nhất
#print(max([],default='kteam')) #nếu rỗng thì sẽ ra giá trị default
#a=(i for i in range (2))
#print(sorted(a,reverse=True)) #sẽ in ngược lại giá trị