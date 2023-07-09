

class LC2Pointer:

    @staticmethod
    def is_palindrome_2(s: str) -> bool:
        """
        Approach 2 with 2 pointers
        """
        s1 = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(s1)
        left, right = 0, n - 1

        while left < right:
            if s1[left] != s1[right]:
                return False

            left, right = left + 1, right - 1

        return True

    @staticmethod
    def is_palindrome_1(s: str) -> bool:
        """
        Leet Code # 125

        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
        and removing all non-alphanumeric characters, it reads the same forward and backward.
        Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.
        """
        s1 = "".join(ch.lower() for ch in s if ch.isalnum())
        return s1 == s1[::-1]

