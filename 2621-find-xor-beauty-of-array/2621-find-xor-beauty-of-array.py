class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # n = len(nums)
        # beauties = n ** 3
        # for num in range(beauties):
        #     temp = []
        #     for i in range(32):
        #         if i == 0:
        return reduce(ixor, nums)
                

        