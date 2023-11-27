# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:18:45 2023

@author: OS
"""
from Heaps import Heap

def heapsort(A): # tạo funnction sort bằng heap
    H=Heap() # tạo một đối tượng H trong class Heap()
    n=len(A) # lưu kích thước của mảng 
    for i in range(n): # vòng lặp chạy và sắp xếp A theo kiểu heap
        H.insert(A[i])
    k=n-1 # giảm n và lưu biến k
    for i in range(H._csize): # vong lặp chạy cho đến khi delete hết và giá trị xóa được lưu vào A 
        A[k] = H.deletemax()
        k=k-1
        
A=[63, 250, 835, 947, 651 ,28]

print("Original Array:", A)
heapsort(A)
print()
print("sorted Array:", A)

    