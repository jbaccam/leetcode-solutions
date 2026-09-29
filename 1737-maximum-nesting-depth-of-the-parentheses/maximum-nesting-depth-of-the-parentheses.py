class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        deepest = 0
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                deepest = max(deepest, len(stack))
                stack.pop()
            else:
                continue
        
        return deepest