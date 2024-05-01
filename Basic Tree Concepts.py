#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Node Creation
class Node:
    
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

root=Node(25)

root.left=Node(10)
root.right=Node(15)

root.left.left=Node(5)
root.left.right=Node(3)

root.right.left=Node(8)
root.right.right=Node(9)


# In[17]:


#Level Order Traversal
queue=[root,None]
while queue:
    node=queue.pop(0)
    if node==None:
        print()
        if len(queue)==0:
            break
        queue.append(None)
        continue
    print(node.data,end=' ')
    if node.left: 
        queue.append(node.left)
    if node.right:
        queue.append(node.right)


# In[18]:


def inorder(root):
    if root==None:
        return
    
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)


# In[10]:


def preorder(root):
    
    if root==None:
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)
    


# In[13]:


def postorder(root):
    
    if root==None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')
    


# In[15]:


inorder(root)
print()
preorder(root)
print()
postorder(root)


# In[11]:





# In[ ]:




