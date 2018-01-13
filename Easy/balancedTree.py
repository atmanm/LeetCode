#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as a binary tree in
#which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        [height, bal] = self.getHeight(root)
        return bal

    def getHeight(self, root):
        if root is None:
            return [0, True]

        [lHeight, lBal] = self.getHeight(root.left)
        [rHeight, rBal] = self.getHeight(root.right)

        if not lBal or not rBal:
            return [0, False]

        if abs(lHeight - rHeight) <= 1:
            return [max(lHeight,rHeight)+1, True]
        else:
            return [max(lHeight,rHeight)+1, False]

if __name__ == "__main__":
    myTree = Tree()
    myTree.createTree()
    print(Solution().isBalanced(myTree.root))
