# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 07:35:35 2023

@author: OS
"""
from QueLinkedListTree import QueLinkedList
class _Node: # tạo class Node cho Tree
    __slots__ = "_element", "_left", "_right"
    
    def __init__(self, element, left=None, right=None):
        # node bao gồm địa chỉ bên trái phải của node và giá trị chứa trong nó 
        self._element = element # giá trị của node
        self._left = left  # địa chỉ bên trái
        self._right = right # địa chỉ bên phải 
        
class _BinaryTree: # tạo class cây nhị phân *Binary Tree
    def __init__(self):
        self._root = None # tạo mặc định root là None nghĩa là ko trỏ đến đâu hết ()
        
    def maketree(self, e, left, right):# tạo node cho cây 
        self._root = _Node(e, left._root , right._root ) # node bao gồm giá trị và địa chỉ trái và phải 
        
    def preorder(self, troot):# duyệt cây nhị phân theo Gốc-trái-phải
        if troot:
            print(troot._element, end=" ")# in ra phần tử sau khi cập nhật vị trí trái hoặc phải của cây 
            self.preorder(troot._left) # đệ quy về vị trí bên trái 
            self.preorder(troot._right)# đệ quy về vị trí bên phải 
            
    def inorder(self, troot):# duyệt cây nhị phân theo Trái -gốc - Phải
       if troot:
           self.inorder(troot._left) # đệ quy về vị trí bên trái 
           print(troot._element, end=" ")# in ra phần tử sau khi cập nhật vị trí trái hoặc phải của cây 
           self.inorder(troot._right)# đệ quy về vị trí bên phải 
    
    def postorder(self, troot):# duyệt cây nhị phân theo Trái phải gốc
        if troot:
            self.postorder(troot._left) # đệ quy về phía bên trái  của node gốc
            self.postorder(troot._right) # dệ quy về phía bên phải của node gốc
            print(troot._element, end=" ")# in ra giá trị của node gốc sau khi cập nhật vị trí
            
    def levelorder(self): # tạo function để duyệt theo level
        Q=QueLinkedList() # kết nối với QueLinkedList đã làm ở P9 và tạo Queue
        t=self._root    # đặt t là root
        print(t._element,end=" ") # in ra giá trị của root
        Q.enqueue(t) #sử dụng thuộc tính enqueue để thêm một phần tử t vào cuối Queue
        while not Q.isempty(): # kt điều kiện nếu Queue không rỗng thực hiện lệnh dưới 
            t =Q.dequeue() # đặt mặc định xóa sau khi ta chèn trái phải của nó
            if t._left: # kiểm tra node con bên trái của t nếu có thì thực hiện in ra giá trị bên trái và chuyển t về cuối queue
                print(t._left._element,end=" ")
                Q.enqueue(t._left)
            if t._right:# kiểm tra node con bên phải của t nếu có thì thực hiện in ra giá trị bên trái và chuyển t về cuối queue
                print(t._right._element,end=" ")
                Q.enqueue(t._right)
                
    def Count(self,troot): # tạo function đếm số node trong Binary Tree(truyền t._root)
        if troot:# nếu Troot không rỗng
            x= self.Count(troot._left) # thực hiện đệ quy troot về bên trái của t và đếm hết bên trái của t kiểm tra lần lượt theo Postorder
            y= self.Count(troot._right)# thực hiện đệ quy troot về bên phải của t và đếm chúng hết bên phải của t
            return x+y+1 # trả về count sau mỗi lần thực hiện đếm node 
        return 0 # trả về 0  nếu như node đó không tồn lại 
    
    def height(self,troot):# tạo function tính chiều cào của cây
        if troot: # nếu troot ko None thì thực hiện 
            x=self.height(troot._left)# đệ quy nhánh bên trái theo troot
            print(x)
            y=self.height(troot._right)# đệ quy nhánh bên phải theo Troot
            print(y)
            if x>y: # kiểm tra  2 nhánh con nhánh nào thì cộng thêm 1
                return x+1
            else:
                return y+1
        return 0 # lệnh thực thi khi troot trả về null nghĩa là node đó thường sẽ là node lá 
            
        
x = _BinaryTree()# tạo đối tượng cây x
y = _BinaryTree()# tạo đối tượng cây y
z = _BinaryTree()# tạo đối tượng cây z
r = _BinaryTree()# tạo đối tượng cây r
t = _BinaryTree()# tạo đối tượng cây t
s = _BinaryTree()# tạo đối tượng cây s
a = _BinaryTree()# tạo đối tượng cây a

x.maketree(40, a, a)# tạo node của cây với node con trái phải là None
y.maketree(60, a, a)# tạo node của cây với node con trái phải là None
z.maketree(20, x, a)# tạo node của cây với node con trái phải là x , a
r.maketree(50, a, y)# tạo node của cây với node con trái phải là a , y
s.maketree(30, r, a)# tạo node của cây với node con trái phải là x , a
t.maketree(10, z, s)# tạo node của cây với node con trái phải là x , a
print("Inorder Traversal:")
t.inorder(t._root)# tạo cây với kiểu duyệt inorder(Trái-Gốc-Phải), trong đó t._root là đối tượng t được gọi mặc định là root trong cây 
print("\n")
print("Postorder Traversal:")
t.postorder(t._root)# tạo cây với kiểu duyệt postorder(Trái-Phải-Gốc), trong đó t._root là đối tượng t được gọi mặc định là root trong cây 
print("\n")
print("Preorder Traversal:")
t.preorder(t._root)# tạo cây với kiểu duyệt preorder(Gốc-Trái-Phải), trong đó t._root là đối tượng t được gọi mặc định là root trong cây 
print("\n")
print("Levelorder Traveral")
t.levelorder()
print("\n")
print("number of Node ")
print(t.Count(t._root))
print("\n")
print("Height of Binary Trees")
print(t.height(t._root)-1)






















            