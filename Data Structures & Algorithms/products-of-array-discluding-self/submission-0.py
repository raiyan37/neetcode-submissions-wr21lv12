class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for n in range(len(nums)):
            i, j = 0, len(nums) - 1
            while i < n:
                output[n] *= nums[i]
                i += 1
            while n < j:
                output[n] *= nums[j]
                j -= 1
        return output


        