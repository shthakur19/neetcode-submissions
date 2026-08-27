class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        countW = set()


        for r in range(len(s)):
            while s[r] in countW:
                countW.remove(s[l])
                l += 1
            countW.add(s[r])
            res = max(r - l + 1,res )
            
        return res
            
            



