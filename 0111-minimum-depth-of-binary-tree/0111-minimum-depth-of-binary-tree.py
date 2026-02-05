# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        count = 1

        while queue:
            for _ in range(len(queue)):  
                node = queue.popleft()

                if not node.left and not node.right:
                    return count

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            count += 1