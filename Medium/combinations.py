#Given two integers n and k, return all possible combinations of k numbers out
#of 1 ... n.

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        numList = list(range(1,n+1))
        resList = []

        self.combineHelper(numList, k, resList, [])

        return resList

    def combineHelper(self, numList, k, resList, curList):
        if k == 0:
            resList.append(curList)
        else:
            for idx, elem in enumerate(numList):
                self.combineHelper(numList[idx+1:], k-1, resList, curList+[elem])

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())

    print(Solution().combine(n,k))
