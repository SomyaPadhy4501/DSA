class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
    


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        lefthalf = self.maxDepth(root.left)
        righthalf = self.maxDepth(root.right)

        return 1 + max(lefthalf +  righthalf)



# Time complexity is O(n)
# For space complexity is its not a skewed tree we get to store all nodes so it is O(n)