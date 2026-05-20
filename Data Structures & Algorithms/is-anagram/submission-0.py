class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s : int = len(s)
        len_t : int = len(t)

        if len_s != len_t:
            return False

        dict_s : Dict[str, int] = {}
        dict_t : Dict[str, int] = {}

        for i in range(len_s):
            if s[i] in dict_s.keys():
                dict_s[s[i]] += 1
            else :
                dict_s[s[i]] = 1

            if t[i] in dict_t.keys():
                dict_t[t[i]] += 1
            else :
                dict_t[t[i]] = 1

        if len(dict_s) != len(dict_t):
            return False

        for key, val in dict_s.items():
            if key not in dict_t.keys() or dict_t[key] != val:
                return False

        return True