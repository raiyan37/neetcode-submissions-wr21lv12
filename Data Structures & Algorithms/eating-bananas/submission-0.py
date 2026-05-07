class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        
        while lo < hi:
            mid, hours = lo + (hi - lo) // 2, 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                hi = mid
            else:
                lo = mid + 1
        
        return lo



        