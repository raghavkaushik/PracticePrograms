#Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# #You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
#Return the merged tree.
#Note: The merging process must start from the root nodes of both trees.

#Link : https://leetcode.com/problems/merge-two-binary-trees/

#Same position nodes need to be added to form a new tree.

#Time Complexity : O(n)

class node:
    def __init__(self,data):
        self.data=data

class solution:
    def mergetrees(self,t1,t2):
        if not t1 and not t2:
            return None

        v1=t1.val if t1 else 0
        v2=t2.val if t2 else 0
        root=node(v1+v2)
        root.left=self.mergetrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergetrees(t1.right if t1 else None, t2.right if t2 else None)
        return root
