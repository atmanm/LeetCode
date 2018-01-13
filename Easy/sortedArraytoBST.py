# Given an array where elements are sorted in ascending order, convert it to a
#height balanced BST

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#class Tree(object):
#    def __init__(self):
#        self.root = None
#        self.array = []
#
#    def createNode(self, data):
#        return TreeNode(data)
#
#    def insert(self, node, data, ch='L'):
#        if node is None:
#            return self.createNode(int(data))
#        if (ch == 'L'):
#            node.left = self.insert(node.left, int(data), ch)
#            return node.left
#        else:
#            node.right = self.insert(node.right, int(data), ch)
#            return node.right
#    def createTree(self, nums):
#        if len(nums) == 0:
#            return
#
#        self.array = nums
#        self.root = self.binaryAdd(0,len(nums)-1, self.root)
#
#    def binaryAdd(self, startIdx, endIdx, root):
#        if endIdx < startIdx:
#            return
#        midIdx = int((startIdx + endIdx)/2)
#        root = self.insert(None, self.array[midIdx])
#
#        root.left = self.binaryAdd(startIdx, midIdx-1, root.left)
#        root.right = self.binaryAdd(midIdx+1, endIdx, root.right)
#
#        return root
#
#    def preorderTraversalUtil(self, root):
#        if root is None:
#            #print ("-1", end=' ')
#            return
#        print(root.val, end=' ')
#        self.preorderTraversalUtil(root.left)
#        self.preorderTraversalUtil(root.right)
#
#    def preorderTraversal(self):
#        self.preorderTraversalUtil(self.root)
#        print()
#
#class Solution(object):
#    def sortedArrayToBST(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: TreeNode
#        """
#        myTree = Tree()
#        myTree.createTree(nums)
#        myTree.preorderTraversal()
#        return myTree.root

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        midIdx = len(nums) // 2
        root = TreeNode(nums[midIdx])
        root.left = self.sortedArrayToBST(nums[:midIdx])
        root.right = self.sortedArrayToBST(nums[midIdx+1:])

        return root


if __name__ == "__main__":
    try:
        array = [x for x in input().strip().split(',')]
    except ValueError:
        array = []

    Solution().sortedArrayToBST(array)
