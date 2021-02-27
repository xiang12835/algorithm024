class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """        
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        
        由于两个数组有序，考虑从后往前比较

        双指针+从后往前
        T: O(m+n)
        S: O(1)
        """

        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n:
           nums1[:n] = nums2[:n]