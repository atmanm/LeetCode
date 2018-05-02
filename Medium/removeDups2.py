#Follow up for "Remove Duplicates":
#What if duplicates are allowed at most twice?

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsDict = {}

        i, count, last = 0, 0, len(nums) - 1
        while i < len(nums):
            count += 1
            try:
                numsDict[nums[i]] += 1
            except KeyError:
                numsDict[nums[i]] = 1
            else:
                if numsDict[nums[i]] > 2:
                    count -= 1
                    if i < last:
                        nums.append(nums.pop(i))
                        last -= 1
                    else:
                        break
                    i -= 1
            i += 1

        return count


if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]

    print(Solution().removeDuplicates(nums))
    print(nums)
