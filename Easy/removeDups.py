# Given a sorted array, remove the duplicates in-place such that each element
# appear only once and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the
#input array in-place with O(1) extra memory.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        readIdx = 1
        writeIdx = 1
        while readIdx < len(nums):
            if nums[readIdx] > nums[readIdx - 1]:
                nums[writeIdx] = nums[readIdx]
                writeIdx = writeIdx + 1
            readIdx = readIdx + 1

        return writeIdx


if __name__ == "__main__":
    try:
        nums = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        nums = []

    print(Solution().removeDuplicates(nums))

