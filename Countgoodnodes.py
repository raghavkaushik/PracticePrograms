#Link : https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#Return the number of good nodes in the binary tree.

#Time complexity : O(n)

#Logic: Preorder- recursive approach, res is set to 1 initially as root node is always a good node.

class solution:
    def goodnodes(self,root):
        def dfs(node,maxval):
            if not node:
                return 0
            res=1 if node.val>=maxval else 0
            maxval=max(node.val,maxval)
            res+=dfs(node.left,maxval)
            res+=dfs(node.right,maxval)
            return res
        return dfs(root,root.val)


