from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram_dict :Dict[str, List[str]] = {}
        anagram_dict = defaultdict(list[str])
        for val in strs:
            count = [0] * 26
            for ch in val:
                count[ord(ch) - ord('a')] += 1
            anagram_dict[tuple(count)].append(val)

        return list(anagram_dict.values())