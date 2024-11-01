class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                k += 1
                i += 1

        return k

# Create an instance of the Solution class
sol = Solution()

# Test the removeElement method
nums = [3, 2, 2, 3]
val = 3
result = sol.removeElement(nums, val)
print(result)