## Description

Given an array ```nums``` containing ```n``` distinct numbers in the range ```[0, n]```, return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only ```O(1)``` extra space complexity and ```O(n)```runtime complexity?

Example 1:
```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.
```
Example 2:
```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.
```
Example 3:
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.
```
Example 4:
```
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1].
1 is the missing number in the range since it does not appear in nums.
 ```

Constraints:
<ul>
<li>n == nums.length</li>
<li>1 <= n <= 104</li>
<li>0 <= nums[i] <= n</li>
<li>All the numbers of nums are unique.</li>
</ul>

## Solution
```We can compute the sum of nums in linear time, and by Gauss' formula, we can compute the sum of the first nn natural numbers in constant time. 
Therefore, the number that is missing is simply the result of Gauss' formula minus the sum of nums, 
as nums consists of the first nn natural numbers minus some number.```

class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

