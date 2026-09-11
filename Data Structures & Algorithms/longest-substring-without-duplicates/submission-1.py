class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myMap = {}
        left = 0
        best_length = 0

        for right in range(len(s)):
            myMap[s[right]] = myMap.get(s[right], 0) + 1

            while myMap[s[right]] > 1:
                
                myMap[s[left]] -= 1
                left += 1
            current_length = right - left + 1
            if current_length > best_length:
                best_length = current_length

        return best_length
        