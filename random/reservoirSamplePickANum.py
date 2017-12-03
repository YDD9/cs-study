# https://leetcode.com/problems/random-pick-index/description/
"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import random
class Solution(object):

    def __init__(self, nums):
        """        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.numsSize = None


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        reservoir = None
        count = 1
        for t, item in enumerate(self.nums):
            if item == target:
                if not reservoir:
                    reservoir = t
                else:
                    j = random.randrange(count)
                    if j < 1:
                        reservoir = t
                count += 1
        return reservoir

    def pick2(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)