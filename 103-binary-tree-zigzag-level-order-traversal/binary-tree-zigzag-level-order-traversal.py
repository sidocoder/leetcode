# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            n = len(queue)
            arr = []
            

            for i in range(n):
                node = queue.popleft()
                arr.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            ans.append(arr)

        def reverse(arr):
            an = []
            n = len(arr)
            for i in range(n -1, -1, -1):
                an.append(arr[i])
            return an
    

        for i in range(len(ans)):
            if i % 2 != 0:
                ans[i] = reverse(ans[i])
        return ans


