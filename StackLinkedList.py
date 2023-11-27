# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:52:44 2023

@author: OS
"""

class _Node : # tạo Node bằng class 
    def __init__(self,element,next): # tạo method mặc định với 2 đối số
        self._element = element  # tạo thuộc tính _element
        self._next = next  # tạo thuộc tính _next
        
class _StackLinkedList:# tạo Stack bằng LinkedList
    def __init__(self): # tạo method mặc định của class
        self._top =None  # tạo thuộc tính _top 
        self._size = 0 # khởi thuộc tính kích thước ban đầu =0 
        
    def __len__(self): 
        return self._size
    
    def isempty(self): # kiểm tra kích thước trống của Stack
        return self._size ==0;
            
    def push(self,e):# tạo method đẩy node vào đầu stack
        newest=_Node(e, None) # tạo Node có tên là newest
        if self.isempty(): # kiểm tra Stack có bị rỗng hay không
            self._top =newest; # nếu đúng thì node đầu là top
        else:              # ngược lại 
            newest._next = self._top  # lấy địa chỉ của top hiện tại trỏ vào newest
            self._top =newest # đưa _top cho node mới thêm 
        self._size +=1 # cập nhật kích thước
        
    def pop(self): # tạo method loại bỏ node 
        if self.isempty(): # kiểm tra nếu Stack trống thì in lệnh dưới
            print("Stack is empty")
        else:
            self._top = self._top._next # đẩy top xuôngs vị trí kế tiếp 
        self._size -=1 # cập nhật kích thước 
        
    def top(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self._top._element
    
    def display(self):
        p=self._top
        while p:
            print(p._element,end="-->")
            p=p._next
        print()
        
L=_StackLinkedList()
L.push(5)
L.push(4)
L.push(3)
L.display()
L.pop() 
L.display()
        
        
        
            
            
        