class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # in case dictionary does not exist yet use defaultdict

        for s in strs:
            count = [0] * 26 # a - z
            
            for c in s:
                count[ord(c) - ord("a")] += 1 # mapping ascii value to index

            result[tuple(count)].append(s) # group all anagrams w this particular count together

            # tuples are immutable, can be used as a key, lists can't
        
        return list(result.values()) # only want to return the values of result not the keys

        