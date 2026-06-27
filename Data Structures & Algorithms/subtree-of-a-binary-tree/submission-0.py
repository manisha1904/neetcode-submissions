# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSubtreeUtil(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot or root.val != subRoot.val:
            return False

        return (root.val == subRoot.val) and self.isSubtreeUtil(root.left, subRoot.left) and self.isSubtreeUtil(root.right, subRoot.right)  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        stack = [root]

        while stack:
            node = stack.pop()
            # stack.pop()

            if self.isSubtreeUtil(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False
