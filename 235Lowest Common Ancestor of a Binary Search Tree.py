##Lowest Common Ancestor of a Binary Search Tree
##Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
##
##2015年8月21日 17:21:51  AC
##zss

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root==p or root ==q:return root
        elif root.val > max(p.val,q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < min(p.val,q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
