
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return ""
        count_t = Counter(t)
        res = [-1, -1]
        min_len = 10004
        l, r = 0, 0
        have, need = 0, len(count_t)
        window = {}
        for r in range(len_s):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in count_t and count_t[ch] == window[ch]:
                have += 1
            while have == need:
                if (r-l+1) < min_len:
                    min_len = (r-l+1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and count_t[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]