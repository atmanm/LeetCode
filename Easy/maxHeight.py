#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root
#node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        if leftHeight > rightHeight:
            return 1 + leftHeight
        else:
            return 1 + rightHeight

if __name__ == "__main__":
    myTree = Tree()
    myTree.createTree()
    print(Solution().maxDepth(myTree.root))
