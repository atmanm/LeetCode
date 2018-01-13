#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root
#node down to the nearest leaf node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return self.getMinHeight(root)

    def getMinHeight(self,root):
        if root is None:
            return 0

        lHeight = self.getMinHeight(root.left)
        rHeight = self.getMinHeight(root.right)

        if root.left is None or root.right is None:
            return lHeight + rHeight + 1
        else:
            return min(lHeight,rHeight)+1

if __name__ == "__main__":
    myTree = Tree()
    myTree.createTree()
    print(Solution().minDepth(myTree.root))
