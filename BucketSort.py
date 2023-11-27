# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 00:44:57 2023

@author: OS
"""

def bucketsort(A): # tạo function thuật toán sắp xếp 
    n=len(A) # đếm kích thước mảng A
    maxelement = max(A) # trả về element lớn nhất trong Array A
    l=[] # tạo một data rỗng
    buckets = [l]*10 # tạo một bucket với kích thước 10  
    for i in range(n): # vòng lặp thực hiện từ 0 - n 
        j=int(n*A[i] / (maxelement+1)) # đặt j là vị trí của các elemnt trong A
        if len(buckets[j])==0: # kiểm tra kích thước của buckets nếu = 0 thực hiện
            buckets[j] = [A[i]] # chèn giá trị tại i trong array vào vị trí j trong bucket
        else: # ngược lại nếu như bucket không trống
            buckets[j].append(A[i]) # ta dùng hàm append để đẩy giá trị ở mảng A vào bucket tại vị trí đã được tính j
    for i in range(10): # trong vòng lặp for 0-9
        insertionsort(buckets[i]) # ta dùng thuật toán insert và sort vào 
    k=0 # tạo k =0
    for i in range(10): # vòng lặp for chạy từ  0 -9
        for j in range (len(buckets[i])): # vòng  lặp j thực hiện
            A[k] = buckets[i].pop(0) # lấy phần tử đầu tiên của bucket và gán nó lại vào mảng A
            k=k+1 # cập nhật k để lấy các phần tử còn lại

def insertionsort(A): # viết một hàm insertsort để sort mảng
    n = len(A) # tạo kích thước mảng A
    for i in range(1,n): #vòng lặp chạy từ 0 - n-1
        cvalue = A[i] # đặt biến cvalue
        position = i # đặt i là position 
        while position > 0 and A[position -1 ]>cvalue :# vòng lặp thực hiện khi tại vị trí > 0 và giá trị trước đó của i phải lớn hơn cvalue
            A[position] = A [position -1] # hoán đổi vị trí i và i -1 
            position -=1 # giảm position mục đích để đưa giá trị tại i về đúng vị trí giảm dần
        A[position] = cvalue #cập nhật vị trí mới của cvalue

A=[63,21,34,61,12,821,1]
print("Original Array:",A)
bucketsort(A)
print("Sorted Array", A)
