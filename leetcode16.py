#16. 3Sum Closest
#env python3
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        length = len(nums)
        cur = nums[0] + nums[length - 1] + nums[1]
        for i in range(1, length):
            beg = 0
            end = length - 1
            while beg < i and end > i:
                sum = nums[beg] + nums[end] + nums[i]
                # update the closest number
                if abs(sum - target) < abs(cur - target): cur = sum
                # move pointer
                if sum > target: end -= 1
                elif sum < target: beg += 1
                else: return cur
                # -4 -1 1 2
        return cur