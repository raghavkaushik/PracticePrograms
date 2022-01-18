#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as:
#a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

#Link : https://leetcode.com/problems/balanced-binary-tree/

#Time complexity : O(n)

# Logic: We are going to follow a bottoms up approach and upwards with keeping a check for each node that it is balanced.Recursive approach.

#Code:

class binarytrees:
    def balancedbinarytree(self,root):
        def dfs(root):
            if not root: return [True,0]
            left,right=dfs(root.left),dfs(root.right)
            if left[0] and right[0] and abs(left[1] + right[1])<=1:
                balanced=True
            else:
                balanced=False
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]

