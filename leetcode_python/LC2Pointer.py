

class LC2Pointer:

    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        """
        Leet code # 392
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string
        by deleting some (can be none) of the characters without disturbing the relative positions
        of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """
        n, m = len(s), len(t)
        i = j = 0

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1

            j += 1

        return i == n


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

