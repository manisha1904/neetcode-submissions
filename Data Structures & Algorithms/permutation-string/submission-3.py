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
        if len1 > len2:
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len1, len2):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1
            l += 1
            
        return matches == 26
