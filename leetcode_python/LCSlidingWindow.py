class LCSlidingWindow:

    @staticmethod
    def len_of_longest_substring(s: str) -> int:
        """
        Leet code # 3
        Given a string s, find the length of the longest substring without repeating characters.
        """
        seen = set()  # hashset to judge whether a char has occurred before
        n = len(s)

        right = -1  # right pointer, initially pointing to the right of the beginning
        answer = 0

        for i in range(n):
            if i != 0:
                seen.remove(s[i - 1])

            while (right + 1) < n and s[right + 1] not in seen:
                seen.add(s[right + 1])
                right += 1

            answer = max(answer, right - i + 1)

        return answer

    @staticmethod
    def min_sub_array_len(target: int, nums: list[int]) -> int:
        """
        Leet code # 209
        Given an array of positive integers nums and a positive integer target,
        return the minimal length of a  subarray whose sum is greater than or equal to target.
        If there is no such subarray, return 0 instead.
        """
        if not nums:
            return 0

        n = len(nums)
        answer = n + 1
        start, end = 0, 0
        total = 0

        while end < n:
            total += nums[end]

            while total >= target:
                answer = min(answer, end - start + 1)
                total -= nums[start]
                start += 1

            end += 1

        return 0 if answer == (n + 1) else answer
