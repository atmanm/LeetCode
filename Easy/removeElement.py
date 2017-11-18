#Given an array and a value, remove all instances of that value in-place and
#return the new length.
#Do not allocate extra space for another array, you must do this by modifying the
#input array in-place with O(1) extra memory.
#The order of elements can be changed. It doesn't matter what you leave beyond
#the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """

        readIdx = 0
        writeIdx = 0
        while readIdx < len(nums):
            if nums[readIdx] != val:
                nums[writeIdx] = nums[readIdx]
                writeIdx = writeIdx + 1
            readIdx = readIdx + 1

        return writeIdx


if __name__ == "__main__":
    try:
        nums = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        nums = []

    val = int(input())

    print(Solution().removeElement(nums, val))

