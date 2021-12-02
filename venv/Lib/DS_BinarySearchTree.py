#Data Structures : Binary Search Tree
#Insertion,Lookup,Breadth First Search,Depth First Search

#Code:
import collections


class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class bst:
    def __init__(self):
        self.root=None

    def insertion(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            current=self.root
            if data<current.left:
                if current.left==None:
                    current.left=node(data)
                current=current.left
            if data>current.right:
                if current.right==None:
                    current=current.right

    def lookup(self,data):
        if self.root==None:
            print("Empty Tree")
            return False
        else:
            current=self.root
            while(current):
                if current.data==data:
                    return current
                else:
                    if data>current.data:
                        current=current.right
                    if data<current.data:
                        current=current.left
        return True

    def breadthfirstsearch(self):
        if self.root==None:
            return False
        queue=collections.deque()
        lst=[]
        queue.append(self.root)
        while(queue):
            current=queue.pop()
            lst.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    @staticmethod
    def depthfirstsearch(lst,node):
        lst.append(node.data)
        if node.left:
            depthfirstsearch(lst,node.left)
        if node.right:
            depthfirstsearch(lst,node.right)
