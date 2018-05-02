#Suppose an array sorted in ascending order is rotated at some pivot unknown to
#you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#Write a function to determine if a given target is in the array.
#The array may contain duplicates.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                return True

            while start < mid and nums[start] == nums[mid]:
                start += 1

            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().search(nums, target))
