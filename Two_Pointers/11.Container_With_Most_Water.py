class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n1 = 0
        n2 = len(height)-1
        area = 0
        while n1 < n2 : 
            shorter = height[n1] if height[n1] <= height[n2] else height[n2]
            area = max(area, shorter*(n2 - n1))
            if height[n1] < height[n2] : # increase shorter one 
                n1+=1
            else :
                n2-=1
                
        return area
