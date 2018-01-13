#Given a binary tree, check whether it is a mirror of itself (ie, symmetric
#around its center).
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric
#But the following [1,2,2,null,3,null,3] is not

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSameTree(root.left, root.right)
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and \
                   self.isSameTree(p.left, q.right) and \
                   self.isSameTree(p.right,q.left)
        return p is q

if __name__ == "__main__":
    p = Tree()
    p.createTree()
    print(Solution().isSymmetric(p.root))
