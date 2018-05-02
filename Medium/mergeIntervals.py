#Given a collection of intervals, merge all overlapping intervals.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i = 0
        while True:
            if i >= len(intervals) - 1:
                break
            if intervals[i].end >= intervals[i+1].start:
                intervals[i].end = max(intervals[i+1].end, intervals[i].end)
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

if __name__ == "__main__":
    inputStr = input().strip()
    inputList = eval(inputStr)
    intervals = [Interval(s,e) for [s,e] in inputList]
    outputIntervals = Solution().merge(intervals)
    outputList = [[interval.start, interval.end] for interval in outputIntervals]

    print(outputList)
