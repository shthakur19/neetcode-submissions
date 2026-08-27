class Solution:
    def isValid(self, s: str) -> bool:
        closed = []
        closedList = {')':'(', '}': '{', ']':'['}
        for i in s:
            if i in closedList:
                if closed and closedList[i] == closed[-1]:
                    closed.pop()
                else:
                    return False
            else:
                closed.append(i)
        
        return len(closed) == 0 



        