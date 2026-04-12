import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = re.sub(r'[^a-z0-9]',"",s.lower())
        s1 = s[::-1]
        res2 = re.sub(r'[^a-z0-9]',"",s1.lower())
        if (res1 == res2):
            return True
        else:
            return False