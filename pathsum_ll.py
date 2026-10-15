# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,targetSum,path,ans):
        if root is None:
            return None

        path.append(root.val)
        if root.left is None and root.right is None:
            if sum(path)==targetSum:
                ans.append(path.copy())
        else:
            l=self.helper(root.left,targetSum,path,ans)
            r=self.helper(root.right,targetSum,path,ans)
        path.pop()

    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        # base case
        if root is None:
            return []

        path=[]
        ans=[]
        self.helper(root,targetSum,path,ans)
        return ans

        

