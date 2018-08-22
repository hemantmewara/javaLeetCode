class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = 0
        str = ""
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                a = 0
                while i + a < j - a:
                    if s[i + a] == s[j - a]:
                        a += 1
                        continue
                    else:
                        break
                if i + a >= j - a:
                    str = s[i: j + 1] if (j - i + 1) > result else str
                    result = max(result, j - i + 1)
        return str

solution = Solution()
print(solution.longestPalindrome("abbaddddd"))