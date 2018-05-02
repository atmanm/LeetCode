#Given an array of integers sorted in ascending order, find the starting and
#ending position of a given target value.
#Your algorithm's runtime complexity must be in the order of O(log n).
#If the target is not found in the array, return [-1, -1].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchHelper(start, end, searchRight):
            if start == end and nums[start] == target:
                return  start
            if start > end:
                return -1
            med = (start+end)//2
            if nums[med] == target:
                if searchRight:
                    if med == 0 and nums[end] == target:
                        return end
                    if nums[med+1] > target:
                        return med
                    newStart = med + 1
                    newEnd = end
                else:
                    if med == 0 and nums[start] == target:
                        return start
                    if nums[med-1] < target:
                        return med
                    newStart = start
                    newEnd = med - 1
            elif nums[med] < target:
                newStart = med + 1
                newEnd = end
            else:
                newStart = start
                newEnd = med - 1

            return searchHelper(newStart, newEnd, searchRight)

        leftIndex = searchHelper(0, len(nums)-1, False)
        if leftIndex == -1:
            return [-1, -1]
        rightIndex = searchHelper(0, len(nums)-1, True)
        return [leftIndex, rightIndex]

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().searchRange(nums,target))
