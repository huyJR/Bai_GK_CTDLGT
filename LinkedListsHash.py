# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:08:31 2023

@author: OS
"""

class _Node: # định nghĩa lớp node 
    __slots__ = 'element', 'next'# xác định danh sách thuộc tính của hai đối tượng trong node 

    def __init__(self, element, next):
        self.element = element
        self.next = next

class LinkedList: # định nghĩa lớp Linkedlist ,lớp quản lý danh sách liên kết 
    def __init__(self): # phương thức khởi tạo của lớp linkedlist 
        # khởi tạo danh sách rỗng 
        self._head = None
        self._tail = None
        self._size = 0
# Phương thức này trả về kích thước(số lượng phần tử)của danh sách liên kết bằng cách truy cập vào thuộc tính self._size.
    def __len__(self):
        return self._size
# kiểm tra danh sách liên kết có rỗng hay không 
    def isempty(self):
        return self._size == 0

    def addlast(self, e): # thêm một phần tử mới vào cuối danh sách liên kết 
        newest = _Node(e, None) # Tạo một nút(node) mới newest với giá trị e và tham chiếu None.
        if self.isempty():# Kiểm tra xem danh sách liên kết có rỗng hay không.
#Nếu danh sách rỗng, thì self._head được gán bằng newest, tức là newest trở thành nút đầu tiên của danh sách.
            self._head = newest
#Nếu danh sách không rỗng, thì self._tail.next được gán bằng newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1 #tăng self._size lên 1 để cập nhật kích thước danh sách.

    def display(self):#để hiển thị các phần tử trong danh sách liên kết.
        p = self._head #Khởi tạo một biến p để duyệt qua danh sách, bắt đầu từ nút đầu tiên 
        while p: # bắt đầu vòng lặp để duyệt qua danh sách 
            print(p.element, end='-->') # in ra giá trị của nút (node) hiện tại 
            p = p.next #Di chuyển p đến nút kế tiếp trong danh sách bằng cách thay đổi tham chiếu của p.
        print() #n ra một dòng trống sau khi đã hiển thị danh sách.

    def addfirst(self,e) :# thêm phần tử vào đầu danh sách liên kết 
        newest = _Node (e, None) # Tạo một nút(node) mới newest với giá trị e và tham chiếu None.
        if self.isempty():# Kiểm tra xem danh sách liên kết có rỗng hay không.
#Nếu danh sách rỗng, thì self._head và self._tail được gán bằng newest, tức là newest trở thành nút đầu tiên và cuối của danh sách.
            self._head = newest 
            self._tail = newest
        else:#Nếu danh sách không rỗng
#thiết lập thuộc tính next của đối tượng newest để trỏ đến nút đầu tiên hiện tại của danh sách
            newest.next = self._head 
#cập nhật self._head để trỏ đến newest và newest trở thành nút đầu tiên của danh sách, và danh sách được mở rộng ra phía trước.
            self._head = newest
        self._size +=1
    
    def search (self , key ):
        p= self._head # tạo một biến p và trỏ nó đến vị trí đầu tiên 'head' của danh sách 
        index=0 # khởi tạo biến index có giá trị bằng 0
        while p : # vòng lặp while để duyệt qua danh sách (list)
            if p.element== key : # kiểm tra xem giá trị của nút(node) hiện tại có bằng giá trị key hay không
                return index # tìm thấy key thì trả về giá trị của biến index
            p=p.next # sau mỗi lần kiểm tra thì chuyển con trỏ p sang nút (node) tiếp theo , bằng cách thay đổi tham chiếu của p
            index = index+1 # tăng giá trị của biến index lên 1 để theo dõi vị trí phần tử trong danh sách 
        return -1  
    
    def insertsorted(self,e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest 
        else: 
            p=self._head
            q=self._head
            while p and p.element<e:
                q=p
                p=p.next
            if p == self._head :
                newest.next = self._head
                self._head = newest 
            else:
                newest.next = q.next
                q.next = newest 
        self._size +=1
        
    def addany(self, e, position):# thêm một phần tử vào danh sách liên kết
        newest = _Node(e, None) # tạo một đối tượng mới newest kiểu  node giá trị dữ liệu e tham chiếu đến null 
        p = self._head # khởi tạo biến p và gán bằng head để trỏ đến đầu list
        i = 1 # khởi tạo biến i với giá trị 1 để đếm vị trị hiện tại của con trỏ p đến danh sách 
        while i < position - 1:
#Trong mỗi vòng lặp, con trỏ p được di chuyển đến nút kế tiếp trong danh sách bằng cách thay đổi tham chiếu của p.
            p = p.next
            i = i + 1#Biến i được tăng lên 1 sau mỗi lần lặp để theo dõi vị trí hiện tại của con trỏ p.
        newest.next = p.next# thiết lập thuộc tính next của newest để trỏ đến nút kế tiếp của p, tức là nút ban đầu ở vị trí position
        p.next = newest# thiết lập thuộc tính next của p để trỏ đến newest,  newest sẽ được nối vào sau p.
        self._size += 1#cập nhật số lượng phần tử trong danh sách sau khi thêm phần tử mới.
     
    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return None  
        e = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e
    
    def removelast(self):
        if self.isempty():
            print('List is empty')
            return None 
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p.next
            i += 1
        self._tail = p
        p = p.next
        e = p.element
        self._tail.next = None
        self._size -= 1
        return e
    
    def display(self):
        p = self._head
        while p:
            print(p.element, end='-->')
            p = p.next
        print()

        
L = LinkedList()  # Tạo một đối tượng LinkedList

L.addlast(7)  # Thêm các phần tử vào danh sách
L.addlast(4)
L.addlast(12)

#L.display()  # Hiển thị danh sách
print('Size:', len(L))  # In ra kích thước của danh sách

L.addlast(8)
L.addlast(3)

#L.display()
print('Size:', len(L))

