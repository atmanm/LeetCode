#Given an array of integers that is already sorted in ascending order, find two
#numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add
#up to the target, where index1 must be less than index2. Please note that your
#returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution and you may not
#use the same element twice.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l, r = 0, len(numbers) - 1
        while l <= r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1, r+1]

if __name__ == "__main__":
    array = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().twoSum(array, target))
