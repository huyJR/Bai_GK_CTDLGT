# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:15:11 2023

@author: OS
"""
#tạo function in ra lũy thừa 2 của các số 
"""
#bài 4
#cách 1 : dùng công thức 
def caculate_itr(n):# tạo function 
    while n>0: # dùng while để lặp lại các phép tính bên dưới
        k=n**2 
        print(k)
        n=n-1 # giảm n đến khi while kết thúc
        
#cách 2: dùng đệ quy
def caculate_itr(n):
    while n>0: # n+1
        k=n**2 # 1        #O(n)
        print(k) # 1
        caculate_itr(n-1) #1  # hàm này sẽ lặp vô cùng do dùng while 
        
caculate_itr(5) # call hàm truyền đối số lên function """

# bài 5
"""
def caculate_itr(n):
    if n>0: # n+1
        print("so n luc đâu",n)
        caculate_itr(n-1)
        k=n**2 # 1        #O(n)
        print(k) # 1
        print("so n lúc sau ",n)
        
caculate_itr(5)"""

# bài 6 thuạt toan cay 
"""
def caculate_itr(n):
    if n>0: # n+1
        print("so n luc đâu",n)
        caculate_itr(n-1)
        k=n**2 # 1  
        print("so n lúc sau ",n)#O(n)
        print(k) # 1
        caculate_itr(n-1)
        
caculate_itr(5)"""
"""
#bài 9:dùng đệ quy để tính tổng N số hạng đầu 
def sum_rec(n):
    if n==0:# điều kiện để ngắt đệ quy 
        return 0
    else:
        return sum_rec(n-1)+n # đệ quy giảm dần và cộng với n tr khi giảm 
    
    
num= input("Enter number:") # sử dụng hàm input để nhập vào số cần tính 
n=int(num)                 # ép kiểu int số nguyên 
print(sum_rec(n)) """


# bài 11 : 

def factorial_rec(n):
    if n==0:# điều kiện để ngắt đệ quy 
        return 1
    else:
        return factorial_rec(n-1)*n # đệ quy giảm dần và nhân với n tr khi giảm 
    
    
num= input("Enter number:") # sử dụng hàm input để nhập vào số cần tính 
n=int(num)                 # ép kiểu int số nguyên 
print(factorial_rec(n))














