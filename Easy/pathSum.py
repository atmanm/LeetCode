#Given a binary tree and a sum, determine if the tree has a root-to-leaf path
#such that adding up all the values along the path equals the given sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree

class Solution(object):
    def hasPathSum(self, root, mySum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if all([mySum == root.val, root.right is None, root.left is None]):
            return True

        return self.hasPathSum(root.left, mySum-root.val) or \
               self.hasPathSum(root.right, mySum-root.val)

if __name__ == "__main__":
    myTree = Tree()
    myTree.createTree()

    try:
        mySum = int(input('Enter Sum: ').strip())
    except:
        mySum = 0

    print(Solution().hasPathSum(myTree.root, mySum))
