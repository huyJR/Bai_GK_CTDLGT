# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:33:57 2023

@author: OS
"""

class Heap: # class Heap 
    def __init__(self): # tạo function mặc định
        self._maxsize = 10 # tạo kích thước max là 10
        self._data = [1]*self._maxsize # tạo data chứa dữ liệu ( các eleemnt)
        self._csize = 0 # tạo csize mặc định là 0
    
    def __len__(self): # tạo hàm trả về kích thước của data
        return len(self._data) 
    
    def isempty(self):# tạo hàm trả về kích thước data là rỗng
        return len(self._data)==0
    
    def insert(self,e): # tạo function chèn một element vào data tạo thành Heap
        if self._csize == self._maxsize:# nếu kích thước của csize = max thì ta in ra không còn chỗ để chứa e
            print("no space in heap") 
            return 
        self._csize+=1 #ngược lại thì kích thước sẽ tăng lên 1
        hi=self._csize # tạ biến hi và kích thước được lưu vào hi
        while hi > 1 and e > self._data[hi//2]: # vong lặp thực hiện hi >1 và kt giá trị e > giá trị được cha hay không 
            self._data[hi]=self._data[hi//2]# nếu lớn hơn thì chuyển giá trị con với cha
            hi=hi//2 # chuyển vị trí với nhau 
        self._data[hi]=e # trả về vị trí của hi  sau khi cập nhật 
        
    def max(self):# tạo function để làm vị trí max(hay là gốc cho heap)
        if self._csize ==0: # kt nếu csize rỗng thì Heap sẽ không có bất kì phần tử nào
            print("Heap is Empty")
            return
        return self._data[1] # ngược lại ta sẽ trả về phần tử đầu tiên là gốc(Max)
    
    def deletemax(self): # tạo function xóa một phần từ trong heap 
        if self._csize == 0:# kt nếu heap không có phần tử nào trả về rỗng
            print("heap is empty")
            return 
        e = self._data[1] # ngược lại nếu có ta đặt e là gốc và cũng là max
        self._data[1]= self._data[self._csize]# ta đổi giá trị đầu và cuối heap (do lúc csize sẽ là vị trí cuối)
        self._data[self._csize]=-1 # tại vị trí cuối sau khi đổi đặt là -1
        self._csize = self._csize -1 # sau đó ta giảm kích thước đi 1 do phần tử cuối đã bị xóa
        i=1 # tạo i =1 , j gấp đôi i
        j=i*2
        while j<=self._csize: # vòng lặp while chạy nệu < kích thước cuẩ heap
            if self._data[j]<self._data[j+1]: # nếu giá trị vị trí thứ j nhỏ hơn vị trí kế nó thì j tăng lên 1
                j+=1
            if self._data[i] < self._data[j]:# nếu giá trị vị trí i nhỏ hơn vị trí thứ j thì hoán đổi 2 vị trí này cho nhau 
                temp = self._data[i] 
                self._data[i]=self._data[j]
                self._data[j]=temp
                i=j # cho i = j 
                j=i*2 # cập nhật j sau khi hoán đổi 
            else:
                break
        return e
    
    
S = Heap()
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
S.insert(18)

print(S._data)
#S.deletemax()
print()
print(S._data)