#Given a binary tree, return the bottom-up level order traversal of its nodes'
#values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree import Tree
class Solution(object):
    levelList = []
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.levelOrderHelper(root, 0)
        #Save the level order list and clear it. Leetcode uses the same object
        #for all testcases and the levelList gets reused
        retList = list(reversed(self.levelList))
        self.levelList[:] = []
        return retList

    def levelOrderHelper(self, root, height):
        if root is None:
            return
        try:
            self.levelList[height].append(root.val)
        except IndexError:
            self.levelList.append([root.val])

        self.levelOrderHelper(root.left, height + 1)
        self.levelOrderHelper(root.right, height + 1)

if __name__ == "__main__":
    myTree = Tree()
    myTree.createTree()
    print(Solution().levelOrderBottom(myTree.root))
