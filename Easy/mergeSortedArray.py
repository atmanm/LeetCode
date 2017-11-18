#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
#sorted array.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            nums1[:] = []
            [nums1.append(x) for x in nums2]
            return
        elif n == 0:
            return

        i,j = 0,0
        nums1[m:] = []
        nums2[n:] = []

        while j < n:
            if i < m:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    nums1.insert(i,nums2[j])
                    m += 1
                    i += 1
                    j += 1
            else:
                nums1.append(nums2[j])
                j += 1

        return


if __name__ == "__main__":
    try:
        nums1 = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        nums1 = []

    m = int(input())

    try:
        nums2 = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        nums2 = []

    n = int(input())

    Solution().merge(nums1, m, nums2, n)

    print(nums1)
