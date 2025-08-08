# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        ## O(n^2) solution
        if not root:
            return 0
        self.val = 0
        def dfs(node, currentSum):
            if not node:
                return
            
            currentSum += node.val 
            if currentSum == targetSum:
                self.val += 1
            
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
        
        def visitAll(node):
            if not node:
                return
            dfs(node, 0)
            visitAll(node.left)
            visitAll(node.right)

        visitAll(root)
        return self.val

        #O(n) optimal solution but space complexity is O(n) for using the dictionary

        from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path = 0 
        self.pathSum = defaultdict(int)
        self.pathSum[0] = 1

        def dfs(node , cursum):
            if not node:
                return       
            cursum += node.val
            self.path += self.pathSum[cursum - targetSum]
            self.pathSum[cursum] += 1
            dfs(node.right , cursum) or dfs(node.left , cursum)
            self.pathSum[cursum] -= 1
        
        dfs(root , 0)
        return self.path


        

        





        