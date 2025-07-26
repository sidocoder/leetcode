class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # counter = Counter(coins)
        # return sum(coins) + 1
        # [1,2,3,4,11]
        coins.sort()
        pre_sum = 0
        for i in range(len(coins)):
            if coins[i] > pre_sum + 1:
                break
            pre_sum +=coins[i]
        return pre_sum + 1
