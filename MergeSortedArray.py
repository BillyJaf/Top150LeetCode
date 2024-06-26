class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        placement = m + n - 1

        while (pointer2 >= 0):
            if (pointer1 >= 0):
                if (nums2[pointer2] >= nums1[pointer1]):
                    nums1[placement] = nums2[pointer2]
                    pointer2 -= 1
                    placement -= 1
             
                else:
                    nums1[placement] = nums1[pointer1]
                    pointer1 -= 1
                    placement -= 1
            else:
                nums1[placement] = nums2[pointer2]
                pointer2 -= 1
                placement -= 1
