# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:20:51 2023

@author: OS
"""

class _QueuesArray: # tạo class Queues với Array( sử dụng các tính chất đặc trưng của array )
    def __init__(self): # method mặc định 
        self._data = [] # tạo một queues rỗng 

    def __len__(self): # method trả về kích thước của queue
        return len(self._data) # sử dụng hàm len để kích thước
            
    def isempty(self):  # tạo method trả về kiểm tra kích thước queue rỗng
        return len(self._data)==0 # sử dụng len kết hợp với toán tử == để kiểm tra kích thước rỗng
    
    def enqueue(self,e): # tạo method thêm vào phần tử vào queues
        return self._data.append(e) # dùng append để thêm một phần tử vào queues 
    
    def dequeue(self): # tạo method xóa phần tử đầu hàng queues 
        if self.isempty(): # kiểm tra xem queues có rỗng hay không
            print("queues is empty") # nếu rỗng thực hiện lệnh print
            return              # kết thúc method và không thực hiện gì cả 
        return self._data.pop(0) # ngược lại dùng method pop có sẵn để xóa phần tử đầu queues 
    
    def first(self): # tạo method lưu phần tử đầu hàng queues
        if self.isempty():
            print("queues is empty")
            return
        return self._data[0] # lưu giá trị đầu vào first
    
    def display(self): # in ra queues
        print(self._data)
        
Q=_QueuesArray()
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(6)
Q.enqueue(5)
Q.display()
Q.dequeue()
Q.display()