class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if i.isalnum():
                s1=s1+i
        s2=s1.lower()
        print(s2)
        left=0
        right=len(s2)-1
        while left<right:
            if s2[left]!=s2[right]:
                return False
            left=left+1
            right=right-1
        return True
        