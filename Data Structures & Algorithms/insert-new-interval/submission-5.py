class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        insert = False

        for i in intervals:
            if i[1] < newInterval[0]:
                newList.append(i)
                if intervals[-1][1]==i[1]:
                    newList.append(newInterval)
            elif i[0] > newInterval[1]:
                if not insert:
                    newList.append(newInterval)
                    insert = True
                newList.append(i)
            else:
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])

  
        return newList if newList else [newInterval]
        