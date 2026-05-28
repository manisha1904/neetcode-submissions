class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        length = len(s)
        max_f = l = 0
        for r in range(length):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
        