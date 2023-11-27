# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:13:09 2023

@author: OS
"""

class _Node: # tạo class Node 
    def __init__(self,element, next): 
        self._element = element 
        self._next = next 
        
class QueLinkedList: # tạo queues bằng Linked List 
    def __init__(self): # tạo method mặc định của Queues 
        self._front= None # tạo thuộc tính phẩn tử đứng đầu tiên của queue
        self._rear = None # tạo thuộc tính phần tử đứng cuối cùng của queue
        self._size = 0 # tạo kích thước mặc định là 0 
    
    def __len__(self): # tạo method khởi tạo trả về kích thước 
        return self._size
    
    def isempty(self): # tạo method kiểm tra kích thước rỗng của _QueueLinkedList
        return self._size == 0
    
    def enqueue(self, e): # tạo method thêm một phần tử vào cuối queues
        newest = _Node(e, None) # tạo node 
        if self.isempty():  # kiểm tra queues có rỗng hay không
            self._front = newest # nếu đúng cái thêm vào sẽ là cái đầu tiên 
            self._rear = newest 
        else: 
            self._rear._next =newest # ngược lại thì ta lấy địa của của newest trỏ vào phần tử cuối 
        self._rear=newest # chuyển vị trí cuối thành node được thêm 
        self._size +=1  # cập nhật kích thước queue
        
    def dequeue(self): # tạo method xóa phần tử đầu tiên trong queues
        if self.isempty(): # kiểm tra queues có rỗng hay không
            print("queue is empty") # thực hiện lệnh print nếu rỗng
            return # sau đó thì không thực hiện gì cả
        e=self._front._element # lưu phần tử đầu tiên vào biến e
        self._front = self._front._next # chuyển vị trí đầu đến phần tử nằm đằng sau
        self._size -=1 # cập nhật kích thước sau khi giảm 
        return e # trả về phần tử đã lưu 
    
    def first(self): # tạo method lấy phần tử đầu 
        if self.isempty(): # kiểm tra xem queues có rỗng hay không
            print("queue is empty") # thực hiện lệnh print nếu rỗng
            return
        return self._front._element# lưu giá trị của phần tử đầu vào method
    
    def display(self): 
        p=self._front
        while p:
            print(p._element,end="<--")
            p=p._next
        print()
        
   
        
            
    