# import string

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        ch = '@'
        for s in strs:
            result += str(len(s)) + ch + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            cnt = ""
            while i < len(s) and s[i] >= '0' and s[i] <= '9' and s[i] != '@':
                cnt += s[i]
                i += 1
            i += 1
            length = int(cnt)
            result.append(s[i:i+length])
            i += length
        return result


