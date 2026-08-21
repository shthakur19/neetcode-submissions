class Solution:
    def isPalindrome(self, s: str) -> bool:
        bla = ''.join(c.lower() for c in s if c.isalnum())
        # print(bla)
        return ''.join(reversed(bla)) == bla 
         

        