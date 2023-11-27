# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:41:18 2023

@author: OS
"""
class _DeQueArray: # tạo DeQue sử dụng array 
    def __init__(self): # tạo method mặc định của StackArray 
         self._data=[] # tạo một data rỗng
         
    def isempty(self): # tạo method  kiểm tra Stacks rỗng
         return self._data == 0 # trả về Stacks ==0 nghĩa là lúc này stack ko có bất cứ phần tử nào
     
    def __len__(self): # tạo method trả về số phần tử trong stack
         return self._data 
    
    def addfirst(self,e):# tạo method thêm một phần tử vào đầu Deque
        self._data.insert(0, e) # sử dụng method insert để thêm một tủ vào đầu DeQuee
    
    def addlast(self,e):# tạo method thêm một phần tử vào cuối Deque
        self._data.append(e)# sử dụng method append để thêm một tủ vào cuối DeQue
        
    def removefirst(self): # tạo method xóa phần tử đầu 
        if self.isempty(): # kiểm tra xem DeQue có rỗng hay không 
            print("DeQue is empty")
            return 
        return self._data.pop(0) # thực nếu không rỗng và dùng pop để loại bỏ một tử đầu pop(0)
    
        
    def removelast(self): # tạo method xóa phần tử cuối
        if self.isempty(): # kiểm tra xem DeQue có rỗng hay không 
            print("DeQue is empty")
            return 
        return self._data.pop() # thực nếu không rỗng và dùng pop để loại bỏ một tử cuối pop()
    
    
    def first(self): # đã được giải thích 
        if self.isempty():
            print("DeQue is empty")
            return 
        return self._data[0]
    
    def last(self):# đã được giải thích
        if self.isempty():
            print("DeQue is empty")
            return 
        return self._data[-1]
    
    def display(self):
        print(self._data)
    
    
D=_DeQueArray()
D.addfirst(5)
D.addfirst(12)
D.addfirst(1)
D.addlast(4)
D.addlast(3)
D.display()
D.removefirst()
D.display()
a=D.first()
print(a)
b=D.last()
print(b)
    
    