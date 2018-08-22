class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        left = (int)(length - 1) / 2
        right = (int)(length / 2)
        i = 0
        nums1Index = 0
        nums2Index = 0
        while (i < left):
            if nums1[nums1Index] <= nums2[nums2Index] and nums1Index < len(nums1):
                nums1Index += 1
            elif nums1[nums1Index] > nums2[nums2Index] or nums2Index < len(nums2):
                nums2Index += 1
            i += 1
            
        a1 = min(nums1[nums1Index], nums2[nums2Index])
        if (left == right):
            a2 = a1
        else:
            a2 = min(nums1[nums1Index], nums2[nums2Index])
        return (a1 + a2) / 2

solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))