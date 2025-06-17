
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        

########### ------------> Optimized solution above solution is unoptimized runs for O(n^2)

  def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0 ]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced , 1 + max(left[1] , right[1])]

        return dfs(root)[0]
