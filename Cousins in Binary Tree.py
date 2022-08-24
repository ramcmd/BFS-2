# TC: O(n)
# SC: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q = deque()
        
        q.append(root)
        
        count = 0
        while q:
            size = len(q)
            temp = []
            
            for _ in range(size):
                node = q.popleft()
                temp.append(node.val)
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.right.val == x and node.left.val == y):
                        return False

                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
                
            if x in temp and y in temp:
                return True
            
                