# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:54:46 2023

@author: OS
"""

class _StackArray: # tạo class Stack 
    def __init__(self): # tạo method mặc định của StackArray 
        self._data=[] # tạo một data rỗng
        
    def isempty(self): # tạo method  kiểm tra Stacks rỗng
        return self._data == 0 # trả về Stacks ==0 nghĩa là lúc này stack ko có bất cứ phần tử nào
    
    def __len__(self): # tạo method trả về số phần tử trong stack
        return self._data 
    
    def push(self,e): # tạo method đẩy giá trị vào Stacks 
        self._data.append(e) # sử dụng hàm append để đưa một phần tử vào data
        
    def my_custom_pop(self): # tạo một method xóa phần tử đỉnh của Stacks
        if self.isempty(): # kiểm tra Stack có rỗng thì thực hiện lệnh dưới
            print("Stacks is empty") # in ra chuỗi String trong print 
            return
        return self._data.pop() # nếu không rỗng thì ta dùng phương thức pop() có sẵn trong python để xóa ptu đỉnh trong stack
    
    def top(self): # tạo method dùng để lưu giá trị đỉnh vào method trên 
        if self.isempty():
            print("Stacks is empty")
            return
        return self._data[-1]  # trả về phần tử đỉnh 
    
    def display(self): # method để in các phần tử trong stack 
        print(self._data)
        
S=_StackArray() # tạo đối tượng S 
S.push(3) # đẩy giá trị 3 vào 
S.push(4)
S.push(6)
S.push(7)
S.display() # in ra các ptu trong Stack
value_top=S.top() # lưu giá trị đỉnh được lưu trong method top()
print(value_top) # in ra giá trị được luuw trong top 
a=S.my_custom_pop() # xóa phần tử đỉnh và đồng thời giá trị của nó cũng được lưu trong method 
print # in ra phần tử vừa bị xóa 
S.display()

       