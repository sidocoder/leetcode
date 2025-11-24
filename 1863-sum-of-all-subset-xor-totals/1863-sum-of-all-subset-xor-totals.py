class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        OR = 0
        for x in nums:
            OR |= x
        return OR * (1 << (len(nums) - 1))