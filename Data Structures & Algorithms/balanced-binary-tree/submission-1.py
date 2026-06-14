# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root:Optional[TreeNode], result: list) -> int:
        if not root:
            return 0

        leftHeight = self.height(root.left, result)
        rightHeight = self.height(root.right, result)

        if abs(leftHeight - rightHeight) > 1:
            result[0] = False

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        result = [True]
        self.height(root, result)
        return result[0]

        # leftHeight = self.height(root.left)
        # rightHeight = self.height(root.right)

        # return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)