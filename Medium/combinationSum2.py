# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
#Each number in C may only be used once in the combination.

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.combination2Helper(candidates, target, [], result)
        return result

    def combination2Helper(self, candidates, target, curList, result):
        print(candidates, target, curList, result)
        if target == 0 and curList not in result:
            result.append(curList)
        elif target < 0:
            return

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            self.combination2Helper(candidates[i+1:],
                                    target-candidates[i],
                                    curList+[candidates[i]],
                                    result)

if __name__ == "__main__":
    candidates = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().combinationSum2(candidates, target))
