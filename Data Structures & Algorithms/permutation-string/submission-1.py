def isPalindromePresent(substr: str, s1: str) -> bool:
    cnt1 = [0] * 26
    cnt2 = [0] * 26
    for i in range(len(s1)):
        cnt1[ord(s1[i]) - ord('a')] += 1
    for i in range(len(substr)):
        cnt2[ord(substr[i]) - ord('a')] += 1

    for i in range(26):
        if cnt1[i] != cnt2[i]:
            return False
    return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        l, r = 0, len1 - 1
        while r < len2:
            substr = s2[l:l+len1]
            print(substr)
            if isPalindromePresent(substr, s1):
                return True
            l += 1
            r += 1
        return False