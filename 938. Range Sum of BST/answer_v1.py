from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        val = root.val

        if root.val < low or root.val > high:
            val = 0

        return val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)