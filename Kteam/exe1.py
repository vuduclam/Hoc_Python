# n = int(input())
""" arr = map(int, input().split())
a=list(arr)
max=a[0]
for i in a:
    if i>max:
        max=i 
a.remove(max)
nhi=a[0]
for i in a:
    if i>nhi:
        nhi=i 
print(nhi) """

""" arr = map(int, input().split())
b=set(arr)
a = sorted(list(b))
# print(a[-2])
print(b) """

#xem năm đó có phải là năm nhuận hay không và trả về True False
""" def is_leap(year):                                                                
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
       leap = True
    return leap
year = int(input())
print(is_leap(year)) """

#nhập 3 in ra 123
""" n = int(input())
a = [i for i in range(1,n+1)]
for i in a:
    print(i,end='') """

""" n = int(input())
a = [i for i in range(1,n+1)]
print(*a,sep='') """

#in list
""" x = int(input())
y = int(input())
z = int(input())
n = int(input())
d=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                d.append([i,j,k])
print(d) """

""" x = int(input())
y = int(input())
z = int(input())
n = int(input())
d=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(d) """

#in tên dọc có số điểm thấp thứ 2 (trùng tên thì sắp theo bảng chữ cái)
""" b=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    b.append([name,score])
sec = sorted(set([i[1] for i in b]))[1]
name= [i[0] for i in b if i[1] == sec]
print(*sorted(name),sep='\n' ) """

n = int(input())
student_marks = {}
for _ in range(n):
    name, line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(scores)
# query_name = input()