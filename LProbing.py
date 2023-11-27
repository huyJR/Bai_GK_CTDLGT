# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:58:05 2023

@author: OS
"""

class HashLinearProbe: # tạo class HashLinearProbe
    def __init__(self): # hàm khởi tạo mặc định
        self.hashtable_size = 10 # khởi tạo với kích thước là 10
        self.hashtable = [0]*self.hashtable_size # tạo Array hashtable
    
    def hashcode(self,key): # tạo function hashcode để lấy số đơn vị của element
        return key % self.hashtable_size 
    
    def lprobe(self,element): # tao function sắp xếp vị trí cho các element
        i=self.hashcode(element) # đặt i là giá trị sau khi lấy đơn của element và cũng là vị trí trong hashtable
        j=0 # khởi tạo j=0
        while self.hashtable[(i+j) % self.hashtable_size]!=0: # vòng lặp thực hiện khi tại vị trí trùng với vị trí đã có
            j=j+1 # nếu trùng thì tăng j lên 1 đồng nghĩa e sẽ chuyển đến vị trí kế tiếp
        return (i+j) % self.hashtable_size # trả về vị trí đã tìm sau khi cập nhật
    
    def insert(self, element): # chèn một element vào hashtable
        i=self.hashcode(element) # đặt i là giá trị sau khi lấy đơn của element và cũng là vị trí trong hashtable
        if self.hashtable[i] == 0: # kt nếu hashtable tại vị trí i chưa có element nào thì thực hiện chèn
            self.hashtable[i]= element
        else: # ngược lại nếu có thì ta thực hiện kiểm tra vị trí tại đó và tìm vị trí mới cho element cần chèn
            i=self.lprobe(element)  # cập nhật i với vị trí mới cần chèn thông qua hàm lprobe
            self.hashtable[i] = element # chèn element vào hashtable
            
    def search(self, key): # thuật toán tìm kiếm elemnt trong hashtable
        i= self.hashcode(key) # vị trí của key được lưu vào i
        j=0 # cho j = 0 
        while self.hashtable[(i+j) % self.hashtable_size]!=key:# vòng lặp thực hiện nếu giá trị tại vị trí đó khác key
            if self.hashtable[(i+j) % self.hashtable_size] == 0: # nếu tại vị trí đó mà = 0 thì trả về False đồng nghĩa là không tìm thấy
                return False
            j=j+1 # ngược lại thì ta tăng j lên 1 để tìm đến vị trí tiếp theo 
        return True # nếu tìm được trả về True
    
    def display(self):
        print(self.hashtable)
        

H = HashLinearProbe()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)   
H.insert(34)
H.insert(86)
H.insert(28)
H.insert(96)
H.display()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        