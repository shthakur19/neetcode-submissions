class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            while l < r and not self.aNum(s[l]):
                l+= 1
            while r > l and not self.aNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1 , r-1
        
        return True

    def aNum(self, l):
        return (ord('A')<= ord(l)<= ord('Z') or
        ord('a')<= ord(l)<= ord('z') or
        ord('0')<= ord(l)<= ord('9'))
        