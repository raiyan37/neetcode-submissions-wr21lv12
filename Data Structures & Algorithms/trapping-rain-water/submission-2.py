class Solution:
    def trap(self, height: List[int]) -> int:
        

        l, r = 0, len(height) - 1
        ml, mr = 0, 0
        water = 0

        while (l < r):

            if (height[l] < height[r]):
                if (height[l] > ml):
                    ml = height[l]
                else:
                    water += ml - height[l]
                l += 1
            else:
                if (height[r] > mr):
                    mr = height[r]
                else:
                    water += mr - height[r]
                r -= 1
                
        return water


            

            
            