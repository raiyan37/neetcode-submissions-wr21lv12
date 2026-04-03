class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} # val : index

        for i, n in enumerate(nums): # enumarate lets you keep track of both index and value
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []