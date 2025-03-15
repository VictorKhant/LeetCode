class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            l_temp = s[l].isalnum()
            r_temp = s[r].isalnum()
            if not l_temp or not r_temp:
                if not l_temp:
                    l += 1
                if not r_temp:
                    r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else: 
                l += 1
                r -= 1
        return True

                
                