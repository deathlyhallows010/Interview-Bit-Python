# https://www.interviewbit.com/problems/merge-overlapping-intervals/ 

# Merge Overlapping Intervals

# Given a collection of intervals, merge all overlapping intervals.
# For example:
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# Make sure the returned intervals are sorted

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(intervals):
        res = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            # print(interval)
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res 