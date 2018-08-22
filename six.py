class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = [["" for i in range((len(s) / (2 * numRows - 2) + 1) * (numRows - 1))] for i in range(numRows)]
        sum = 0
        i = 0
        j = 0
        l = 0
        while sum < len(s):
            if l < numRows + numRows - 2:
                if l < numRows:
                    result[i][j] = s[sum]
                    i += 1
                else:
                    result[i - 2][j + 1] = s[sum]
                    j += 1
                    i -= 1
                l += 1
                sum += 1
            else:
                l = 0
                i = 0
                j += 1
        a = ""
        for i in result:
            for j in i:
                a += j
        return a

solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))