class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap -> key is element, value is count
        # if the count is greater or equal to k, append to a new list
        # return that list


        counts = {}
        top_k_elements = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        sorted_items = sorted(counts.items(),  key = lambda item: item[1], reverse = True)

        for i in range(k):
            top_k_elements.append(sorted_items[i][0])

        return top_k_elements


        

        