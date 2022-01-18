#Invert Binary Tree
#Link:https://leetcode.com/problems/invert-binary-tree/

#Problem statment : swap each left node to right node

#Time complexity: O(n)

class solutions:
    def inverttree(self,root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.inverttree(root.left)
        self.inverttree(root.right)
        return root
