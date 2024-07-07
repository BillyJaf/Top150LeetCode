"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        distance = nums[0]

        for num in nums:
            if distance < 0:
                return False

            if num > distance:
                distance = num

            distance -= 1
        
        return True
