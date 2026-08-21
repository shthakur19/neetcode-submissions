class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        sString =set()
        l= 0
        for r in range(len(s)):
            while s[r] in sString:
                sString.remove(s[l])
                l += 1
            sString.add(s[r])
            res = max(res,r-l+1)
        
        return res

        