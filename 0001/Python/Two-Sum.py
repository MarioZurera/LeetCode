class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            if n in diff:
                return (diff[n], i)
            diff[target - n] = i
        return (-1, -1)
