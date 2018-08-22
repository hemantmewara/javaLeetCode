class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = []
        length = 0
        for i in s:
            if i not in str:
                str.append(i)
            else:
                length = max(length, len(str))
                str = str[str.index(i) + 1: ]
                str.append(i)
        return max(length, len(str))

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))