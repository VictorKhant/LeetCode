# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        isLeftToRight = True

        while queue:
            levels = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if isLeftToRight:
                    levels.append(node.val)
                else:
                    levels.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)    
            result.append(list(levels))
            isLeftToRight = not isLeftToRight
        return result