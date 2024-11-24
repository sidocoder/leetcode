class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        current_max, current_min = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            temp_max = current_max
            current_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
            current_min = min(nums[i], nums[i] * temp_max, nums[i] * current_min)
            max_product = max(max_product, current_max)
        
        return max_product
