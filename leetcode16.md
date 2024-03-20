## Leetcode 16
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:<br>
Input: nums = [-1,2,1,-4], target = 1

Output: 2<br>
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2: <br>
Input: nums = [0,0,0], target = 1

Output: 0
<br>Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:<br>
3 <= nums.length <= 500<br>
-1000 <= nums[i] <= 1000<br>
-104 <= target <= 104


## method
first you should sort the list. `O(nlgn)` <br>
And then you can use two pointers to help you.<br>
left **element** right <br>
you should check all elments in the list. <br>
if left + right + element < sum : move left pointer <br>
else: move right pointer


