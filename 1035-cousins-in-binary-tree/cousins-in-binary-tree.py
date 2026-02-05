# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue = deque([root])
        hashh = defaultdict(list)
        depth = {}
        depth[root.val] = 0 

        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    hashh[node.val].append(node.left.val)
                    depth[node.left.val] = depth[node.val] + 1
                if node.right: 
                    queue.append(node.right)
                    hashh[node.val].append(node.right.val)
                    depth[node.right.val] = depth[node.val] + 1
            
        if depth.get(x) != depth.get(y):
            return False

        for key,val in hashh.items():
            if x in val and y in val:
                return False
        return True


        