def my(a,b='kk'):  
    if a:
        return (f'{a} {b}')                             #return trả về giá trị và các câu lệnh sau nó dừng, phải gán biến c cho hàm
    return (f'Kenny {b}')   

 
c= my('asad')                                            #vì asad là True nên đúng return trên
print (c)