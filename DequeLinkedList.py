# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:26:25 2023

@author: OS
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:13:09 2023

@author: OS
"""

class _Node: # tạo class Node 
    def __init__(self,element, next): 
        self._element = element 
        self._next = next 
        
class _DeQueLinkedList: # tạo queues bằng Linked List 
    def __init__(self): # tạo method mặc định của Queues 
        self._front= None # tạo thuộc tính phẩn tử đứng đầu tiên của queue
        self._rear = None # tạo thuộc tính phần tử đứng cuối cùng của queue
        self._size = 0 # tạo kích thước mặc định là 0 
    
    def __len__(self): # tạo method khởi tạo trả về kích thước 
        return self._size
    
    def isempty(self): # tạo method kiểm tra kích thước rỗng của _QueueLinkedList
        return self._size == 0
    
    def addfirst(self, e): # tạo method thêm một phần tử vào đầu queues
        newest = _Node(e, None) # tạo node 
        if self.isempty():  # kiểm tra queues có rỗng hay không
            self._front = newest # nếu đúng cái thêm vào sẽ là cái đầu tiên 
            self._rear = newest 
        else: 
            newest._next= self._front # ngược lại thì ta lấy địa của của newest trỏ vào phần tử đầu
        self._front =newest # chuyển vị trí đầu  thành node được thêm 
        self._size +=1  # cập nhật kích thước 
        
    def addlast(self, e): # tạo method thêm một phần tử vào cuối queues
            newest = _Node(e, None) # tạo node 
            if self.isempty():  # kiểm tra queues có rỗng hay không
                self._front = newest # nếu đúng cái thêm vào sẽ là cái đầu tiên 
                self._rear = newest 
            else: 
                self._rear._next =newest # ngược lại thì ta lấy địa của của newest trỏ vào phần tử đầu
            self._rear =newest # chuyển vị trí cuối thành node được thêm 
            self._size +=1  # cập nhật kích thước queue
        
    def removelast(self): # tạo method xóa phần tử đầu tiên trong queues
        if self.isempty(): # kiểm tra queues có rỗng hay không
            print("queue is empty") # thực hiện lệnh print nếu rỗng
            return # sau đó thì không thực hiện gì cả
        p=self._front
        i=1
        while i<len(self)-1: # vòng lặp để xác đinh p cuối 
            p=p._next
            i+=1
        e=self._rear._element # lưu phần tử đầu tiên vào biến e
        self._rear = p # chuyển vị trí cuối đến vị trí p kế cuối 
        p=p._next # chuyển p sang p cuối (lúc này là p cần delete)
        self._rear._next = None # trỏ địa trỉ không có gì
        self._size -=1 # cập nhật kích thước sau khi giảm 
        return e # trả về phần tử đã lưu 
    
    def removefirst(self): # tạo method xóa phần tử đầu tiên trong queues
        if self.isempty(): # kiểm tra queues có rỗng hay không
            print("queue is empty") # thực hiện lệnh print nếu rỗng
            return # sau đó thì không thực hiện gì cả
        e=self._front._element # lưu phần tử đầu tiên vào biến e
        self._front = self._front._next
        self._size -=1
        return e # trả về phần tử đã lưu 
    
    
    def first(self): # tạo method lấy phần tử đầu 
        if self.isempty(): # kiểm tra xem queues có rỗng hay không
            print("queue is empty") # thực hiện lệnh print nếu rỗng
            return
        return self._front._element# lưu giá trị của phần tử đầu vào method
    
    def last(self): # tạo method lấy phần tử cuối
        if self.isempty(): # kiểm tra xem queues có rỗng hay không
            print("queue is empty") # thực hiện lệnh print nếu rỗng
            return
        return self._rear._element# lưu giá trị của phần tử đầu vào method
    
    def display(self): 
        p=self._front
        while p:
            print(p._element,end="-->")
            p=p._next
        print()
        
Q = _DeQueLinkedList()

Q.addfirst(8)
Q.addfirst(6)
Q.addfirst(12)
Q.addfirst(15)
Q.addlast(13)
Q.display()
Q.removefirst()
Q.removelast()
Q.display()
        
            
    