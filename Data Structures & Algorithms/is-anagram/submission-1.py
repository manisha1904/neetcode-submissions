class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s : int = len(s)
        len_t : int = len(t)

        if len_s != len_t:
            return False

        count = [0] * 26
        for i in range(len_s):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True