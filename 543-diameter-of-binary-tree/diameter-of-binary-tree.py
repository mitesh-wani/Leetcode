# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def height(node):
            if not node :
                return 0
            left_height=height(node.left)
            right_height=height(node.right)
            curr_path=left_height+right_height
            self.max_diameter = max(self.max_diameter, curr_path)

            return 1+max(right_height,left_height)    
        height(root)
        return self.max_diameter