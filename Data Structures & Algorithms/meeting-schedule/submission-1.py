"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def compare(a):
    return a.start 

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        intervals.sort(key = compare)
        lastEnd = intervals[0].end

        for i in intervals[1:]:
            #print(start,end)
            if lastEnd <= i.start:
                lastEnd = i.end
            else:
                return False

        return True

        
