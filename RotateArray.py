"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution(object):
    def reverse(self, nums, leftPointer, rightPointer):
        holder = nums[0]
        while (leftPointer < rightPointer):
            holder = nums[leftPointer]
            nums[leftPointer] = nums[rightPointer]
            nums[rightPointer] = holder
            leftPointer += 1
            rightPointer -= 1


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
