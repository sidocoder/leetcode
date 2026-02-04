# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return None

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            arr = []
            n = len(queue)
         
            for i in range(n):
                num = queue.popleft()
                arr.append(num.val)
                
                if num.left: queue.append(num.left)
                if num.right: queue.append(num.right)
            average = (sum(arr) / len(arr))
            ans.append(average)
        return ans



        