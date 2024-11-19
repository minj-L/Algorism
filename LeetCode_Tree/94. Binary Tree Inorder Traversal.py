# 트리 문제이지만 dfs로 풀이다! (스택이나 재귀함수로 풀이) 
# 이번문제는 중위순회, 전위, 후위로도 풀어보자!
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        reuslt = []
        
        def dfs(node):
            if node is not None:
                dfs(node.left) # 
                reuslt.append(node.val)
                dfs(node.right)
            
        dfs(root)
        return reuslt