# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 00:02:13 2023

@author: OS
"""
# 1 Data types , float , interger 
"""x=10 
print(x)
print(type(x))
y=10.25 
print(y)
print(type(y))"""
# 3 string  data type 
"""
s = '''hi, my name is Huy''' #ngoài ra ta có thể dùng 3 ''' để đóng một chuỗi string như này 
s = '''hi, "my name" is Huy''' # hoặc ta có thể kết hợp với nhau để phục vụ cho nhu cầu người dùng như này 
print (s)
print(type(s))"""

# 4 Boolean & None 
  #Boolean
"""x=True 
print(type(x))
print(x)

x=10 
y=20 
z=x>y
print(type(x))
print(type(y))
print(type(z))
  # None 
x=None # khởi tạo biến x là None (None là kiểu trống biểu thị vắng hoặc không giá trị , không xác định được )
print(x) # in ra giá trị x 
print(type(x)) # in ra kiểu dữ liệu của x 
 
x1=10 # khởi biến x1 với giá trị là 10 
y=print(x1) # khởi tạo biến y = in ra (giá trị x)
print(y) # in ra y biến y lúc này không xác định được""" 
# 6 opearator comparision 
"""x=10
y=20 
print (x>y) # ta có thể dử dụng toán tử so sánh trực tiếp ngay trong hàm in --> nó sẽ trả về true hoặc false
x1="hello"
x2="python"
print(x1<x2) # ngoài ra ta có thể so sách các kí tự thông qua độ dài , giống khác nhau --> python có thể nhận dạng một cách nhanh chóng 
x3='aaa'
x4='aad'
print(x3>x4)
x5='a'
y5='k'
print(ord(x5)) # ta sẽ thêm hàm ord đầy là hàm trả về giá trị unicode --> trả về mã 97 
print(ord(y5)) # trả về mã --> 107 """

#7 Logical operator 
"""
x = True
y = False
result = x and y
print(result)  # Kết quả: False 

x1 = True
y1 = False
result1 = x1 or y1
print(result1)  # Kết quả: True 

x2 = True
result2 = not(x2)
print(result2)  # Kết quả: False"""

#8 Input() function 
"""x=input("nhap vao so x :")# hàm input cho phép ta nhập một chuỗi string mang kiểu dữ liệu  mặc định là string 
y=input("nhap vao so y :")# mang kiểu string 
print(x+y) # kết quả sẽ là 23 nếu ta nhập x=2 , y=3 
print(int(x)+int(y)) # nếu mún cộng theo ý ta mong muốn ta sẽ phải ép kiểu """

#9 print() function 
"""print("hello\npython") # hàm print kết hợp với \n để chỉ xuống dòng 
print ("hello\tpython") # /t tạo khoảng trắng
print ('hello'+'python') # cộng 2 chuỗi string 
print('hello'*5) # ta có thể dùng toán tử nhân(*) để in ra 5 lần hello 
x=20 
y=10
z=15 
print("giá trị của 3 số là :" , x, y, z) # có thể in ra 1 lúc nhiều đối tượng 
#10 if , if-else , elif 
          #if
x = 10
if x > 5:
    print("x lớn hơn 5")
    
        #if-else 
x = 3
if x > 5:
    print("x lớn hơn 5")
else:
    print("x không lớn hơn 5")
    
        #elif 
x = 7
if x > 10:
    print("x lớn hơn 10")
elif x > 5:
    print("x lớn hơn 5, nhưng không lớn hơn 10")
else:
    print("x không lớn hơn 5")"""

#11 range() function 
"""numbers = range(5) # python sẽ tự mặc định giá trị đầu tiên là 0 -> n-1 nếu ta đưa giá trị đầu vào 
print(list(numbers))  # Kết quả: [0, 1, 2, 3, 4]

numbers = range(2, 10)
print(list(numbers))  # Kết quả: [2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = range(0, 11, 2)
print(list(even_numbers))  # Kết quả: [0, 2, 4, 6, 8, 10]"""

#12 while()&for() loop 
"""count = 0
while count < 5: # vòng lặp từ count =0 ->4 
    print("Count:", count) # in  ra giá trị lặp 
    count +=1          # tăng biến đếm lên 1 

fruits = ["apple", "banana", "cherry"] # ta sẽ tạo một danh sách trước khi đưa vào vòng lặp 
for fruit in fruits: # vòng lặp chạy từ trái qua phải tương ứng với các vị trí 0 , 1 ,2 
    print(fruit)"""
# 13 break & continue 
          # break
"""l=[12,3,4,65,7,2]
n=int(input("nhap vào so cần tìm: ")) # vào số cần tìm bằng hàm input 

for i in l : # vòng lặp chạy trong Linked List l 
    print(i,n) # in ra từng giá trị trong l, và số cần tim n khi chạy vòng lặp 
    if i==n: # đặt điều kiện nếu bằng với giá trị tìm 
        print("Found!") # trả về là in ra "Found!" 
        break  # thoát ngay khỏi vòng lặp nếu đk đúng 

           # continue 
for i in range(5): # vòng lặp chạy từ 0-4 
    if i == 2:  # nếu i==2 thì thực hiện lệnh dưới
        continue # bỏ qua vòng lặp hiện tại 
    print(i) # in ra giá trị i """

# 15 using List 
"""l=[2, 'hello', 10.35] # tạo một danh sách liên kết 
print(l) # in ra list 
print(type(l)) # in ra kiểu dữ liệu của l 

print(l[1]) # in ra vị trí thứ 2 tương đương với n-1 
print(l[-1]) # in ra vị trí cuối do trừ -1 nó sẽ lấy ngược lại 
l[1]="python" # thay đổi giá trị trong list 
print(l)    # in ra sau khi thay đổi """

# 17 Tuples Indexing 
"""
t=(3.82, 'hello', 6) # tạo một tuples gồm 3 phần tử 
print(t) # in ra tuples 
print(type(t)) # in ra kiểu dữ liệu tuples 
print(len(t)) # in ra độ dài của tuples 

print(t[1]) # in phần tử thứ 2 
print(t[-1]) # in ra phần tử cuối cùng """

# 18 Membership & identity Operators 
            # Membership 
"""
l=[2, 'hello', 10.35,3,4,6,8] # tạo một danh sách liên kết 
print(3 in l) # kiểm 3 có nằm trong danh sách hay không 
print(7 not in l) # kiểm tra 7 không có trong danh sách đúng không 
             
             # identity 
l1=[12,3,4,65,7,2]
l2=[12,3,4,65,7,2]

print(l1 is l2)# kiểm tra l1 có cùng danh tính hay không
print (l1==l2) # kiểm tra l1 == l2 hay không 
l1=l2 
print(l1 is l2 ) # kiểm tra l1 có cùng danh tính hay không """

# 20 Using Dictionaries 
"""d={'USA':'America', 'UK':[200, 'london'] , 'India':(300)}
print(d)
#print(d[1]) # trường này ta không thể lấy giá trị tự dic bằng cách này 
#print(d['USA']) # dưới đây là cách để lấy giá trị bên phải từ dic 
#print(d['America']) # ta không thể lấy từ trái qua phải trong 1 phần tử dic 

d['Aus']=400 # thêm hoặc gán 1 phần tử vào dic 
print(d)

del(d['UK']) # xóa một phẩn tử trong dic 
print(d)

print(d.keys()) # in ra các từ khóa tìm kiếm 
print(d.values()) # in các giá trị trong dic 

for i in d: # vòng lặp để in ra các phần tử trong d 
    print(i,d[i]) # in ra từ khóa keys() và values() trong dic 

print('USA' in d) # có thể kiểm tra membership  trong dic nhưng ta chỉ có thể kiểm tra bằng key()"""

#22 Writing Function 

"""def display(): # tạo function 
    print("hello") # in ra hello 
    print("python") # in ra python
    
def mysum(a,b): # tạo function mysum với 2 đối số là a , b 
    c=a+b    # tính tổng a b
    return c  # trả về c 
    
    
display() # gọi hàm để in ra trong display 
x=mysum(2, 3) # gọi hàm và truyền tham chiếu a,b và lưu trong biến x
print(x) # in ra x """

# 23 Importing Modules in Python 

"""import math 
from math import sqrt
import math as h

a=h.sqrt(25)
print (a)"""

# 24 Creating Your Own  Modules

"""def display(): # tạo method display 
    print("Modules ABC ") 
    
def myadd(x,y): # tạo method cộng tên myadd
    return x+y """

#26 Defining Class & Creating Objecting 

"""class _Student(): # tạo class Student 
    
    def __init__(self, name,marks,age): # tạo method khởi tạo ban đầu cho class _Student với 3 đối số
        self._name = name # tạo tên thuộc tính _name 
        self._mark = marks # tạo tên thuộc tính _mark
        self._age = age # tạo tên thuộc tính _age 
        
    def __str__(self):  # tạo method chuỗi string 
        return 'this is class of student' # trả về một chuỗi string 
    
    def display(self): # tạo method display 
        print('student name:', self._name) # in ra tên của _name khi được truyền đối số string
        print('student marks:', self._mark) # in ra điểm của  _mark khi được truyền đối số float
        print('student age:', self._age) # in ra tuổi của  _age khi được truyền đối số int 
        
    # cách 1 : truyền tham chiếu bằng cách lưu biến và truyền đối số trực tiếp trong class    
S1=_Student('Huy' , 9.8, 22) # truyền đối số ten , điểm , tuổi của student S1 
S2=_Student('Khanh', 9.5, 19) # truyền đối số ten , điểm , tuổi của student S2
S3=_Student('Cuong', 9.9, 25) # truyền đối số ten , điểm , tuổi của student S2

S1.display() # sử dụng phương thức display trong class để in ra các thông số vừa tham chiếu trên S1 
S2.display()
S3.display()"""


# 27  More on __init__ Method (Constructor)
"""class _Student(): # tạo class Student 
    
    def __init__(self): # tạo method khởi tạo ban đầu cho class _Student với 3 đối số
        self._name ='Huy' # tạo tên thuộc tính _name 
        self._mark = 9.9 # tạo tên thuộc tính _mark
        self._age = 21 # tạo tên thuộc tính _age 
        print("Huy dep trai")
        
   
    def display(self): # tạo method display 
        print('student name:', self._name) # in ra tên của _name khi được truyền đối số string
        print('student marks:', self._mark) # in ra điểm của  _mark khi được truyền đối số float
        print('student age:', self._age) # in ra tuổi của  _age khi được truyền đối số int


S=_Student() # tạo đối tượng S trong class nó sẽ lấy những thuộc tính mặc định trong method __init__ 
S.__init__() # gọi đối tượng chứa các thuốc tính trong method """

# 28 Understanding self Parameter
"""class _Student(): # tạo class Student 
    
    def __init__(myself, name,marks,age): # tạo method khởi tạo ban đầu cho class _Student với 3 đối số
        myself._name = name # tạo tên thuộc tính _name 
        myself._mark = marks # tạo tên thuộc tính _mark
        myself._age = age # tạo tên thuộc tính _age 
        
    def __str__(myself):  # tạo method chuỗi string 
        return 'this is class of student' # trả về một chuỗi string 
    
    def display(abc): # tạo method display 
        print('student name:', abc._name) # in ra tên của _name khi được truyền đối số string
        print('student marks:', abc._mark) # in ra điểm của  _mark khi được truyền đối số float
        print('student age:', abc._age) # in ra tuổi của  _age khi được truyền đối số int 
        
    # cách 1 : truyền tham chiếu bằng cách lưu biến và truyền đối số trực tiếp trong class    
S1=_Student('Huy' , 9.8, 22) # truyền đối số ten , điểm , tuổi của student S1 
S2=_Student('Khanh', 9.5, 19) # truyền đối số ten , điểm , tuổi của student S2
S3=_Student('Cuong', 9.9, 25) # truyền đối số ten , điểm , tuổi của student S2"""

#29 Static and Local Variables

class _Student: # tạo class Student 
    
    def __init__(self, name,marks,age): # tạo method khởi tạo ban đầu cho class _Student với 3 đối số
        self._name = name # tạo tên thuộc tính _name 
        self._mark = marks # tạo tên thuộc tính _mark
        self._age = age # tạo tên thuộc tính _age 
       
        
    def __str__(self):  # tạo method chuỗi string 
        return 'this is class of student' # trả về một chuỗi string 
    
    def display(self): # tạo method display
        print('student name:', self._name) # in ra tên của _name khi được truyền đối số string
        print('student marks:', self._mark) # in ra điểm của  _mark khi được truyền đối số float
        print('student age:', self._age)
        print('student bk:', _Student._college)# in ra tuổi của  _age khi được truyền đối số int 
        
    # cách 1 : truyền tham chiếu bằng cách lưu biến và truyền đối số trực tiếp trong class    
_Student._college = ' BK'
S1=_Student('Huy' , 9.8, 22) # truyền đối số ten , điểm , tuổi của student S1 
S2=_Student('Khanh', 9.5, 19) # truyền đối số ten , điểm , tuổi của student S2
S3=_Student('Cuong', 9.9, 25) # truyền đối số ten , điểm , tuổi của student S2

S1.display()
S2.display()
S3.display()



