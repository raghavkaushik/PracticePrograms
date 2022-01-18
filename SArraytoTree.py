#Link : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

#Time Complexity: O(n)

#Logic: The middle of the sorted array will be the root node and similarly we keep dividing the array based on left and right of mid forming the left and right children.

class node:
    def __init__(self,data):
        self.data=data

class solution:
    def sortedarraytoBST(self,arr):
        def helper(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            root=node(arr[mid])
            root.left=helper(l,mid-1)
            root.right=help(mid+1,r)
            return root

        return helper(0,len(arr)-1)

