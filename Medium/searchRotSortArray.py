#Suppose an array sorted in ascending order is rotated at some pivot unknown to
#you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#You are given a target value to search. If found in the array return its index,
#otherwise return -1.
#You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchHelper(start, end):
            if start > end:
                return -1
            med = ((start+end)//2)
            if nums[med] == target:
                return med
            if nums[0] == target:
                return 0
            if target >= nums[med] and nums[med] >= nums[0]:
                newStart, newEnd = med + 1, end
            elif target >= nums[0] and nums[0] >= nums[med]:
                newStart, newEnd = 1, med - 1
            elif nums[med] >= target and target >= nums[0]:
                newStart, newEnd = 1, med - 1
            elif nums[med] >= nums[0] and nums[0] >= target:
                newStart, newEnd = med + 1, end
            elif nums[0] >= target and target >= nums[med]:
                newStart, newEnd = med + 1, end
            elif nums[0] >= nums[med] and nums[med] >= target:
                newStart, newEnd = 1, med - 1

            return searchHelper(newStart, newEnd)

        return searchHelper(0, len(nums)-1)

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().search(nums, target))
