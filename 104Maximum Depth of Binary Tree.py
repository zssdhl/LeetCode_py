##Maximum Depth of Binary Tree
##Given a binary tree, find its maximum depth.
##The maximum depth is the number of nodes along the longest path
##from the root node down to the farthest leaf node.
##
##2015年8月13日 17:46:52  AC
##zss

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:return 0
        else:return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
