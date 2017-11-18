#Given a sorted array and a target value, return the index if the target is
#found. If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.

class Solution(object):
    array = []
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.array = nums
        return self.binarySearch(0, len(nums)-1, target)

    def binarySearch(self, startIdx, endIdx, target):
        """
        :type startIdx: int
        :type endIdx: int
        :type target: int
        """
        midIdx = int((startIdx + endIdx)/2)

        if midIdx <= startIdx or midIdx >= endIdx:
            #Element not found, figure out where to insert
            if target <= self.array[startIdx]:
                return startIdx
            elif target > self.array[endIdx]:
                return endIdx + 1
            else:
                return midIdx + 1
        if self.array[midIdx] == target:
            return midIdx
        elif self.array[midIdx] > target:
            idx = self.binarySearch(0, midIdx, target)
        else:
            idx = self.binarySearch(midIdx, endIdx, target)

        return idx


if __name__ == "__main__":
    try:
        array = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        array = []

    try:
        target = int(input())
    except ValueError:
        target = 0

    print(Solution().searchInsert(array, target))
