class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)

        total = 0
        l = 0
        r = 1
       
        while r <= (n -1):
            summ = min(nums[l], nums[r])
            total += summ
            l += 2
            r += 2

        return total 


       
        