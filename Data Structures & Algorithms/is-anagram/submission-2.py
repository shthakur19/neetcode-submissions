class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        sC, tC = {},{}
        for i in range(len(s)):
            sC[s[i]] = sC.get(s[i],0) +1
            tC[t[i]] = tC.get(t[i],0) +1
        
        return sC == tC



        