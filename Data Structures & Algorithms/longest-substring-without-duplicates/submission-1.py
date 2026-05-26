class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_dict = {}
        max_len, curr_len, l = 0, 0, 0
        length = len(s)

        for i in range(length):
            ch = s[i]
            if ch not in char_dict.keys():
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                r = char_dict[ch]
                for j in range(l, r+1):
                    del char_dict[s[j]]
                l = r + 1
                curr_len = i - r
            char_dict[ch] = i
        max_len = max(max_len, curr_len)
        return max_len