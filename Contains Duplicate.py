#For better memory complexity- we can use Hash set
# Hash set? A hash set is a data structure that: Stores unique elements.Allows fast operations like add, remove, and check for existence — all in about O(1) time.

Question:
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

```
Pseudocode Code:
Function hasDuplicate(nums):
    Create an empty set called seen

    For each number in nums:
        If the number is in seen:
            Return True (duplicate found)
        Add the number to seen

    Return False (no duplicates found)


Python Code:

from typing import List  # Needed if you're using List[int]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example usage:
def main():
    nums = [1, 2, 3, 3]
    solution = Solution()
    result = solution.hasDuplicate(nums)
    print(result)

main()


Logic Behin this proble:

Break It Into Small Steps
Write steps like:

- Create an empty set
- Go through each number in the list
- If the number is in the set → return True
- If not, add it to the set
- If loop ends → return False
- Try to understand why each step is done.


