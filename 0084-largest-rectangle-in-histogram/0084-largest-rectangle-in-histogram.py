class Solution(object):
    def largestRectangleArea(self, heights):
        stack=[]
        maxarea=0
        n=len(heights)
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                height=heights[stack.pop()]
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                maxarea=max(maxarea,height*width)
            stack.append(i)
        while stack:
            height=heights[stack.pop()]
            if stack:
                width=n-stack[-1]-1
            else:
                width=n
            maxarea=max(maxarea,height*width)
        return maxarea