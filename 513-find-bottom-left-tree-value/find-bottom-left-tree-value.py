# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return []
        
        # queue = deque([root])
        # ans = []

        # while queue:
        #     n = len(queue)
        #     level = []

        #     for i in range(n):
        #         node = queue.popleft()
        #         level.append(node.val)

        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     ans.append(level)

        # n = len(ans)
        # return ans[n-1][0]
        
        
        queue = deque([root])
        ans = root.val

        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                if i == 0:
                    ans = node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return ans