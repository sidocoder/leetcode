from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashh = defaultdict(list)
        
        # Build the hash map to store the indices of each number
        for i in range(len(nums)):
            hashh[nums[i]].append(i)
            
        for key, indices in hashh.items():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if abs(indices[j] - indices[i]) <= k:
                        return True
        return False
