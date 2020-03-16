class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if(n<2):
            return s
        left = 0
        right = 0

        palindrome = [[0]*n for _ in range(n)]

        for j in range(1,n):
            for i in range(0,j):
                innerIsPalindrome = palindrome[i+1][j-1] or j-i<=2
                if(s[i] == s[j] and innerIsPalindrome):
                    palindrome[i][j] = True
                    if(j-i>right-left):
                        left = i
                        right = j

        return s[left:right+1] 
        