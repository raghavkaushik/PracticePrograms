#Data Structures : Binary Search Tree
#Zigzak View, Top View, Boundary View

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

    def zigzak(self):
        if self.root==None:
            return False
        currentlvl=[]
        nextlvl=[]
        lst=[]
        count=1
        currentlvl.append(self.root)
        while(currentlvl):
            current=currentlvl.pop(-1)
            lst.append(current.data)
            if count%2==0:
                if current.left:
                    nextlvl.append(current.left)
                if current.right:
                    nextlvl.append(current.right)
            else:
                if current.right:
                    nextlvl.append(current.right)
                if current.left:
                    nextlvl.append(current.left)
            if len(currentlvl)==0:
                currentlvl,nextlvl=nextlvl,currentlvl
                count+=1
        print(lst)
        return True

    def topview(self):
        d={}
        def traverse(node,key,level):
            if key not in d:
                d[key]=[node,level]
            else:
                if d[key][1]>level:
                    d[key]=[node,level]
            traverse(node.left,key-1,level+1)
            traverse(node.right,key+1,level+1)
        traverse(self.root,0,0)
        print(d)

    def boundaryview(self):
        def printleft(node):
            if node:
                if node.left:
                    print(node.data)
                    printleft(node.left)
                elif node.right:
                    print(node.right)
                    printleft(node.right)

        def printright(node):
            if node:
                if node.right:
                    printright(node.right)
                    print(node.right)
                if node.left:
                    printright(node.left)
                    print(node.data)

        def printleaves(node):
            if node:
                printleaves(node.left)
                if node.left==None and node.right==None:
                    print(node.data)
                printleaves(node.right)
        if self.root==None:
            return False
        else:
            current=self.root
            while(current):
                print(current.data)
                printleft(current.left)
                printleaves(current.left)
                printleaves(current.right)
                printright(current.right)

        return True