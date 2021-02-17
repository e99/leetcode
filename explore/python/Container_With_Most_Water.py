class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxValue=-1
        low=0
        high=len(height)-1
        while low<high:
            maxValue=max(maxValue,min(height[low],height[high])*(high-low))
            if height[low]<height[high]:
                low+=1
            else:
                high-=1
        return maxValue