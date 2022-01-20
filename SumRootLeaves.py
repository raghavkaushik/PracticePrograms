#Link : https://leetcode.com/problems/sum-root-to-leaf-numbers/

#Time Complexity - O(n)

#Logic - Multipy the initial number with 10 and sum the next node to form the number to each path and just sum the number once formed.

class solutions:
    def sumroots(self):
        def sumleaves(node,num):
            if not node:
                return 0
            num=num*10 + node.val
            if not node.left and not node.right:
                return num
            return sumleaves(node.left,num) + sumleaves(node.right,num)
        return sumleaves(self.root,0)