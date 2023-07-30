

class LC2Pointer:
    @staticmethod
    def max_area(height: list[int]) -> int:
        """
        You are given an integer array height of length n. There are n vertical lines drawn
        such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.
        """
        left, right = 0, len(height) - 1
        answer = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            answer = max(answer, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return answer

    @staticmethod
    def two_sum_II(numbers: list[int], target: int) -> list[int]:
        """
        Leet code # 167
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
        find two numbers such that they add up to a specific target number.

        Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.
        """
        low, high = 0, len(numbers) - 1

        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]


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

