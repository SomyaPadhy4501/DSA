class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)
        # longest = ""

        # for i in range(n):
        #     for j in range(i+1, n):
        #         sub = s[i:j]
        #         if sub == sub[::-1]:
        #             if len(sub) > len(longest):
        #                 longest = sub
        # return longest

        n = len(s)
        res = ""
        maxlen = 0
        for i in range(n):
            # for odd palindromes
            l , r = i , i 
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1
            
            # for even palindromes
            l , r = i , i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1
            
        return res

