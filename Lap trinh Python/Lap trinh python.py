# ******************************************************************************************Toán tử
# >=, <=, >, <, ==, !=, and, or, not sẽ ra giá trị True, False
# Falsy bao gồm '', None. 0, 0j
# print(1>2) #sẽ ra False
# print(0 and 2)                    #vế đầu true sẽ trả giá trị thứ 2
# print(3>1 or 2)                     #vế đầu false sẽ trả giá trị thứ 2
# age=34
# print(f'i am {age}')                  #f là địng dạng string, type là string
# print('i am', age)                    #type là tuple
# print('i am ' + str(age))             #type là str
# print('i am {}'.format(age))           #type là str
# username = input ('hay nhap:')
# usd= input('hay nhap: ')                #input sẽ trả về string
# usd= float(input('hay nhap: '))
# print(usd*5)
# a = 8
# b=('i am' + str(a))                           #b là str
# b = ('i am', a)                               # b là tuple
# print(type(b))
# print(ord('a'))                                #hàm lấy mã ascii
#***************************************************************************List
#    0 1 2 3    #thứ tự của list
# -4,-3,-2,-1   #thứ tự của list
#a=[1,2,3,4]
#dir(list)                  #sẽ ra các hàm thuộc list
#print(dir(list))
#del a[2]                      #xóa phần tử thứ 2 trong list
#print(a)
#b=max(a)                    #sẽ lỗi nếu list chứa str và int
#b=min(a)                    #sẽ lỗi nếu list chứa str và int
#***************************************************************************
#from pprint import pprint            #pprint sẽ in ra xuống dòng nếu list đó dài
#a=[1,2,3]
#b=a     
#print(a,b)                              
#print (b is a)                           #True
#b=a.copy()
#print (b is a)                           #False vì b và a nằm trên 2 bộ nhớ khác nhau
#print(id(a),id(b))                        #hàm id kiểm tra vị trí bộ nhớ
#b=a[start:stop;step]                      #lấy ra list mới 