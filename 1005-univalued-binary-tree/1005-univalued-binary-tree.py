# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ls = []
        def bfs(node,ls):
            if not node:
                return 
            # if node.left or node.right:
                # left = node.left
                # right = node.left         
                # if left:
                #     ls.append(left.val)
                # if right:
            ls.append(node.val)
            bfs(node.left,ls)
            bfs(node.right,ls)
            
            return ls

        bfs(root,ls)
        print(ls)
        return len(set(ls)) == 1
                