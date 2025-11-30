# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value: idx for idx, value in enumerate(inorder)}
        
        def helper(in_left, in_right, post_left, post_right):
            if in_left > in_right:
                return None
            
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            in_root_idx = inorder_index[root_val]
            left_size = in_root_idx - in_left
            
            root.right = helper(in_root_idx + 1, in_right, post_left + left_size, post_right - 1)
            root.left = helper(in_left, in_root_idx - 1, post_left, post_left + left_size - 1)
            
            return root
        
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)