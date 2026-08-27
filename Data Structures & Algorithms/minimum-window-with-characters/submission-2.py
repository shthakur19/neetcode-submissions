class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        
        needC, haveC = {}, {}
        l= 0
        minLength = float("infinity")
        res = [-1,-1]

        for i in t:
            needC[i]= 1 + needC.get(i,0)
        need, have  = len(needC), 0

        for r in range(len(s)):
            haveC[s[r]] = 1 + haveC.get(s[r],0)
            
            if s[r] in needC and haveC[s[r]] == needC[s[r]]:
                have += 1

            while have == need:
                if (r-l +1) < minLength:
                    res = [l,r]
                    minLength = r-l +1
                
                haveC[s[l]] -= 1

                if s[l] in needC  and haveC[s[l]] < needC[s[l]]:
                    have -= 1
                l += 1
        l,r = res

        return s[l:r+1] if minLength!= float("infinity") else ""






        
        
        