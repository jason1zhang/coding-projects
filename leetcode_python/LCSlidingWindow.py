class LCSlidingWindow:
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
