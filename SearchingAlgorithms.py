# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:23:34 2023

@author: OS
"""
# Binary Search Intertive

def binary_search(A,key): # tạo function để search giá trị key
    l=0          
    r=len(A)-1
    while l<=r:
        mid = (l+r)//2 # tạo biên mid ở giữa với giá trị khởi tạo bằng giá trị đầu + cuối chia đôi
        print(mid)  
        if key==A[mid] : # nếu key bằng với A tại mid thì trả về vị trí của giá trị vừa tìm được
            return mid  
        elif key < A[mid] : # nếu key < giá trị tại mid thì ta giảm giá trị mid đi 
            r=mid-1
        elif key > A[mid] :
            l=mid+1
    return -1 
        

A=[6,8,12,15,34,54,81]
found = binary_search(A,34)
if found ==-1:
    print ("không tìm thấy số cần tìm")
else:
    print("đã tìm thấy số cần tìm ")
   
#linear Search 
    
"""
def timkiem(A,key): # tạo function tìm kiếm
    index=0;          # tạo biến địa chỉ 
    n=len(A)-1           # tạo kích thước của mảng A
    while index < n:  # vòng lặp thực hiện cho đến khi hết mảng 
        if key==A[index]: # nếu biến cần tìm bằng với giá trị cần tìm thì trả về index
            return index
        index=index+1  # cập nhật biến index 
    return -1    # trả về giá trị -1 nếu như không tìm thấy

A=[23,12,18,11,17,82]
found = timkiem(A, 12)
if found ==-1:
    print("không tìm thấy số cần tìm ")
else:
    print("đã tìm thấy số cần tìm ")"""
  
"""
# Binary Search Recursive

def binarysearch_recursive(A,key,l,r) : # tạo function thuật toán tìm kiếm
    if l>r: # nếu mà duyệt hết mảng mà ko tìm thấy thì trả về -1
        return -1
    else:
        mid = (l+r)//2 # ta thực hiện tạo phần tử mid để tìm kiếm
    if key==A[mid]: # nếu tìm được thì trả về vị trí của phần tử đó
        return mid 
    elif key < A[mid]: # nếu key nhỏ hơn giá trị di chuyển thì ta di chuyển mid sang trái
        return binarysearch_recursive(A, key, l, r-1)
    elif key > A[mid]: # nếu key lớn hơn giá trị di chuyển thì ta di chuyển mid qua phải 
        return binarysearch_recursive(A, key, l+1, r)
        
A=[6,8,12,15,34,54,81]
found = binarysearch_recursive(A,17, 0, len(A)-1)
if found ==-1:
    print ("không tìm thấy số cần tìm")
else:
    print("đã tìm thấy số cần tìm ")   
    """
    
    
    
    
    
    
    
    
    
    
            
            
    
    