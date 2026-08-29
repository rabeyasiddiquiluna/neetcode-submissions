class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        hs = heights + [0]
        best = 0

        for i,h in enumerate(hs):
            while stack and hs[stack[-1]] >= h:
                height = hs[stack.pop()]
                left = stack[-1]+1 if stack else 0
                best = max(best, height *(i - left))
            stack.append(i)

        return best

        