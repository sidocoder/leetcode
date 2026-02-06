# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        queue = deque([root])
        ans = []

        while queue:
            node = queue.popleft()
            ans.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        
        new = set(ans)
        lst = list(new)
        lst.sort()

        if len(lst) >= 2:
            return lst[1]
        else:
            return -1