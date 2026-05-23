def isAlphanumeric(ch: char) -> bool:
    return (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9');
class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        left, right = 0, length - 1

        while left < right:
            left_char = isAlphanumeric(s[left])
            right_char = isAlphanumeric(s[right])
            if left_char and right_char:

                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            else:
                if not left_char:
                    left += 1
                if not right_char:
                    right -= 1
        return True

        