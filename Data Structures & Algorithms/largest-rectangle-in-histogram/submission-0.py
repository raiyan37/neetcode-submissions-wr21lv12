class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                area = width * heights[j]
                max_area = max(area, max_area)   
            stack.append(i)

        while stack:
            j = stack.pop()
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            area = width * heights[j]
            max_area = max(area, max_area)
        
        return max_area


        