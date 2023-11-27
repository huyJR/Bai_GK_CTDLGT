# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:53:13 2023

@author: OS
"""

class _Node: # tạo class Node cho Tree
    __slots__ = "_element", "_left", "_right"
    
    def __init__(self, element, left=None, right=None):
        # node bao gồm địa chỉ bên trái phải của node và giá trị chứa trong nó 
        self._element = element # giá trị của node
        self._left = left  # địa chỉ bên trái
        self._right = right # địa chỉ bên phải 
        
class BinarySearchTree: # tạo class cây nhị phân *Binary Tree
    def __init__(self):
        self._root = None # tạo mặc định root là None nghĩa là ko trỏ đến đâu hết ()
    
    def insert(self,troot,e): # tạo function chèn một node vào cây 
        temp=None  # đặt mặc định biến tạm None 
        while troot: # duyệt troot 
            temp=troot
            if e==troot._element: # nếu biến cần chèn bằng với lại node ở cây thì ta thoát vòng lặp 
                return
            elif e< troot._element: # nếu e nhỏ hơn giá trị troot đang xét thì di chuyển chúng sang trái
                troot = troot._left 
            elif e> troot._element : # nếu e lớn hơn giá trị troot đang xét thì di chuyển chúng sang phải
                troot = troot._right
        n=_Node(e) # đặt n là node cần chèn 
        if self._root: # nếu tồn tại giá trị _root nghĩa là None 
            if e < temp._element : # và e nhỏ hơn giá trị temp (temp này đã duyệt đến vị trí trước vị trí chèn)
                temp._left = n # giá trị temp trỏ lấy n và n đã được đặt địa chỉ ở bên trái temp
            else: # ngược lại 2 trường hợp = và lớn hơn
                temp._right = n # giá trị temp trỏ lấy n và n đã được đặt địa chỉ ở bên phải temp
        else:
            self._root = n # nếu như không phải là None thì là setup n là mặc định là _root 
    
    
    def rinsert(self,troot,e):# tạo function insert bằng đệ quy
        if troot:# nếu tồn tại troot
            if e< troot._element: #và giá trị của e cần chèn < giá trị troot thì thực hiện di chuyển sang trái và đệ quy xét tiếp 
                troot._left = self.rinsert(troot._left, e)
            elif e> troot._element:#và giá trị của e cần chèn > giá trị troot thì thực hiện di chuyển sang phải và đệ quy xét tiếp
                troot._right = self.rinsert(troot._right, e)
        else: # ngược lại nếu không tồn tại troot nghĩa là troot là none thì thực hiện đặt là Node 
            n=_Node(e) # tạo một Node là n 
            troot = n # gán vào troot
        return troot # trả về troot sau khi cập nhật chèn
    
    def inorder(self, troot):# duyệt cây nhị phân theo Trái -gốc - Phải
       if troot:
           self.inorder(troot._left) # đệ quy về vị trí bên trái 
           print(troot._element, end=" ")# in ra phần tử sau khi cập nhật vị trí trái hoặc phải của cây 
           self.inorder(troot._right)# đệ quy về vị trí bên phải 
           
    def search(self,key): # tạo function tìm kiếm 
        troot = self._root # đặt giá trị mặc định là troot
        while troot : # troot tồn tại thì thực hiện lệnh dưới
            if key==troot._element : # nếu key bằng với troot thì trả về True
                return True
            elif key< troot._element: # nếu key < troot thì di chuyển troot đến vị trí bên trái
                troot = troot._left 
            elif key > troot._element:# nếu key > troot thì di chuyển troot đến vị trí bên phải
                troot = troot._right
        return False # nếu tất cả tìm không được thì trả về False 
    
    def rsearch(self,troot,key): # tạo function với 2 tham số truyền vào là troot và key 
        if troot : # nếu troot tồn tại thì thực hiện lệnh dưới 
            if key==troot._element :#nếu key bằng với troot thì trả về True
                return True
            elif key< troot._element: # ngược lại nếu key nhỏ hơn troot thì di chuyển troot sang trái và kiểm tra key
                return self.rsearch(troot._left,key) 
            elif key > troot._element:# ngược lại nếu key lớn hơn troot thì di chuyển troot sang phải và kiểm tra key
                return self.rsearch(troot._right,key) 
        else:
            return False # nếu tất cả tìm không được thì trả về False
    
    def delete(self,e):# tạo function delete
        p=self._root # đặt p là mặc định là root(gốc)
        pp=None # và biến pp  là None
        while p and p._element !=e: # vòng lặp sẽ chạy cho tới khi p gần tới e 
            pp=p # gán pp = p
            if e < p._element: # nếu giá trị e < giá trị p thì thì dịch p sang trái
                p = p._left
            else: # ngược lại e>= p thì dịch sang phải
                p=p._right
        if not p : # nếu p = None trả về False 
            return False
        if p._left and p._right: # kiểm tra bên trái và phải của p
            s = p._left # gán s là phía bên trái của p
            ps = p # gán giá trị tại p là ps
            while s._right: # vòng lặp while khi phía bên phải của s chạy cho tới khi tìm được max của cây (vì là cây inorder nên max trái sẽ nằm bên phải)
                ps =s # cập nhật vị trí của ps sau khi s được tìm
                s=s._right # di chuyển s sang phải
            p._element = s._element #gán giá trị tìm được với giá trị p cần xóa
            p=s #  di chuyển s thành p 
            pp=ps # cập nhật node cha với node vừa mới thay thế
        c=None # tạo biến C là None
        if p._left: # kiểm tra bên trái của p tồn tại  thì  c là bên trái p
            c=p._left 
        else: # ngược lại thì c là phía bên phải của p
            c=p._right
        if p==self._root:  # nếu p là gốc thì Gốc là None
            self._root =None 
        else: # ngược lại 
            if p == pp._left : # nếu p là con trái của nút cha thì nút cha bên trái là c
                pp._left = c 
            else:# nếu p là con phải của nút cha thì nút cha bên phải  là c
                pp._right = c
                
            
            
            
            
        
    
B=BinarySearchTree()
#B._root = B.rinsert(B._root, 10) # định nghĩa node gốc đặt gốc là 10 vì rinsert ta không định nghĩa hàm gốc 
B.insert(B._root, 10)# chèn 10 vào cây và 10 cũng là gốc(root)
B.insert(B._root, 40)# chèn 40 vào cây và lớn hơn 10 nên sẽ nằm bên phải  
B.insert(B._root, 20)# chèn 20 vào cây và lớn 10 và nhỏ hơn 40 nên nằm bên trái 40  
B.insert(B._root, 30)# chèn 30 vào cây trong đó 30 lớn 10 , nhỏ hơn 40, lớn 20 nên nằm bên phải 20
B.insert(B._root, 80)# chèn 80 vào cây trong đó 80 >10 , lớn hơn 40  nên nằm bên phải 40
B.insert(B._root, 54)# chèn 54 vào cây trong đó 54 >10 , lớn hơn 40 và nhỏ 80 nên nằm bên trái 80    
B.inorder(B._root)# thuật toán inoder phù hợp với cách xếp ở trên 
print("\n")  
print(B.rsearch(B._root, 54))
B.delete(54)
B.inorder(B._root)

    
    
    
    
    
    
    