# Given a set of candidate numbers (C) (without duplicates) and a target number
# (T), find all unique combinations in C where the candidate numbers sums to T.
#The same repeated number may be chosen from C unlimited number of times.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        result = []
        self.combinationSumHelper(candidates, target, [], result)

        return result

    def combinationSumHelper(self, candidates, target, curList, result):
        if target == 0:
            result.append(curList)
        elif target < 0:
            return

        for i in range(len(candidates)):
            self.combinationSumHelper(candidates[i:],
                                      target - candidates[i],
                                      curList+[candidates[i]],
                                      result)

if __name__ == "__main__":
    candidates = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().combinationSum(candidates, target))
