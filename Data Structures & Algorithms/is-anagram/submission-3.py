class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount, tCount = {},{}
        for a in range(len(s)):
            sCount[s[a]] = 1 + sCount.get(s[a],0)
            tCount[t[a]] = 1 + tCount.get(t[a],0)
        
        return sCount == tCount
            
        