#Link : https://leetcode.com/problems/validate-binary-search-tree/
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
#Time Comlexity : O(n)

# logic : We will consider two limits to check node, as left nodes must be less than root so the upper bound will be the root value and right nodes must have
#bigger value than the node so this way we will have upper and lower bounds for every node starting both bounds as - and + infinity\

class solution:
    def valid(self,root):
        def checkvalid(node,left,right):
            if not node:
                return True
            if not(node.val<right and node.val>left):
                return False
            return (checkvalid(node.left,left,node.val) and checkvalid(node.right,node.val,right))
        return checkvalid(root,float("-inf"),float("inf"))