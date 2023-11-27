# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 00:07:53 2023

@author: OS
"""

from LinkedListsHash import LinkedList
class HashChain: # tạo class  Hash 
    def __init__(self): # tạo function mặc định với kích thước 
        self.hashtable_size = 10 # tạo kích thước tối đa cho array
        self.hashtable = [0]*self.hashtable_size # tạo data chứa dữ liệu cho hashtable
        for i in range(self.hashtable_size): # vòng lặp để đưa các giá trị vào hashtable
            self.hashtable[i] = LinkedList()
            
    def hashcode(self, key): # tạo mã index cuối của element để đưa vào hashtable 
        return key % self.hashtable_size
    
    def insert(self,element):# phương thức chèn một element vào hashtable
        i = self.hashcode(element) # trả về index của giá trị cần chèn 54, i =4
        self.hashtable[i].insertsorted(element) # chèn giá trị element vào vị trí i vào trong hashtable
    
    def search(self,key): # function tìm kiếm giá trị trong hashtable
        i=self.hashcode(key) # tạo biến i là vị trí của key cần tìm
        return self.hashtable[i].search(key) !=1 # trả về nếu  khác 1 
    
    def display(self): # function display để in ra hashtable
         for i in range(self.hashtable_size): # vòng lặp for để duyệt qua hashtable
             print("[",i,"]", end=" ") # in ra hashtable
             self.hashtable[i].display() # in ra giá trị của table trong LinkedList
         print()
    
H = HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(75)
H.insert(94)
H.display() 