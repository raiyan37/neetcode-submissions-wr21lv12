class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = defaultdict(int)

        for num in nums:
            result[num] += 1

        sorted_items = sorted(result.items(), key=lambda item: item[1], reverse=True)
        
        final_list = []
        
        for i in range(k):
            final_list.append(sorted_items[i][0])
        
        return final_list


        