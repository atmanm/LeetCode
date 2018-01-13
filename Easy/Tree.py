class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def createNode(self, data):
        return TreeNode(data)

    def insert(self, node, data, ch='L'):
        if node is None:
            return self.createNode(int(data))
        if (ch == 'L'):
            node.left = self.insert(node.left, int(data), ch)
            return node.left
        else:
            node.right = self.insert(node.right, int(data), ch)
            return node.right

    def search(self, lis, data):
          # if root is None or root is the search data.
          idx = 0
          if data == 'null':
              return None
          while idx < len(lis):
              [node, used] = lis[idx]
              if node.val == int(data) and used == 0:
                  lis[idx] = [node, 1]
                  return node
              idx += 1

    def preorderTraversalUtil(self, root):
        if root is None:
            #print ("-1", end=' ')
            return
        print(root.val, end=' ')
        self.preorderTraversalUtil(root.left)
        self.preorderTraversalUtil(root.right)

    def preorderTraversal(self):
        self.preorderTraversalUtil(self.root)
        print()

    def createTree(self):
        try:
            array = [x for x in input().strip().split(',')]
        except ValueError:
            array = []

        if len(array) == 1:
            if array[0] == '':
                return
        height = 1
        prevLevel = None
        level = [array[0]]
        myList = []
        while len(level) != level.count('null'):
            print(level)
            if prevLevel is None:
                self.root = self.insert(None, array[0])
                #Append [node, 0] to list. When we populate children of node,
                #we will change it to [node, 1] so we don't use it again
                myList.append([self.root, 0])
            else:
                idx = 0
                while idx < len(prevLevel):
                    ptr = None
                    ptr = self.search(myList, prevLevel[idx])
                    #Append [node, 0] to list. When we populate children of node,
                    #we will change it to [node, 1] so we don't use it again
                    if ptr:
                        if level[2*idx] != 'null':
                            leftChild = self.insert(ptr, level[2*idx], 'L')
                            myList.append([leftChild, 0])
                        if level[2*idx + 1] != 'null':
                            rightChild = self.insert(ptr, level[2*idx+1], 'R')
                            myList.append([rightChild, 0])
                    idx += 1
            prevLevel = level
            nullCount = level.count('null')
            if nullCount:
                indices = [i for i,x in enumerate(level) if x == 'null']
                for index in indices:
                    insertPoint = 2**height + 2**index
                    array[insertPoint:insertPoint] = ['null']*2
            level = array[2**height - 1:2**(height+1) - 1]
            if len(level) != 2**height:
                if len(level) != 0:
                    level += ['null']*(2**height - len(level))
            height += 1


if __name__ == "__main__":
    myTree = Tree()
    myTree.createTree()
    myTree.preorderTraversal()
