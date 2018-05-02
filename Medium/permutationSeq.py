#The set [1,2,3,…,n] contains a total of n! unique permutations.
#By listing and labeling all of the permutations in order,
#given n and k, return the kth permutation sequence.

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        resList = []
        factorialList = [0]*(n+1)
        factorialList[0] = 1

        for i in range(1,n+1):
            factorialList[i] = factorialList[i-1]*i

        numList = list(range(1,n+1))

        k -= 1
        for i in range(1,n+1):
            index = k//factorialList[n-i]
            resList.append(str(numList[index]))
            numList.pop(index)
            k %= factorialList[n-i]

        return ''.join(resList)

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())

    print(Solution().getPermutation(n,k))
