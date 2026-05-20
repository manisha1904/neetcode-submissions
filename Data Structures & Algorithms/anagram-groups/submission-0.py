class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict :Dict[str, List[str]] = {}
        result :List[List[str]] = []
        for val in strs:
            temp_val = "".join(sorted(val))
            if temp_val not in anagram_dict.keys():
                anagram_dict[temp_val] = []
            anagram_dict[temp_val].append(val)

        for key, value in anagram_dict.items():
            result.append(value)
        
        return result