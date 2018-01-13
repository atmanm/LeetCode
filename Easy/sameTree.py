# Given two binary trees, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical and
#the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right,q.right)
        return p is q

if __name__ == "__main__":
    p = Tree()
    p.createTree()
    q = Tree()
    q.createTree()
    print(Solution().isSameTree(p.root,q.root))
