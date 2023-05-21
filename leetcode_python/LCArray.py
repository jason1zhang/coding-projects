from typing import List

class LCArray:
    @staticmethod
    def remove_duplicates_from_sorted_array_II_1(nums: List[int]) -> int:
        """
        Leet code # 80

        Given an integer array nums sorted in non-decreasing order,
        remove some duplicates in-place such that each unique element appears at most twice.
        The relative order of the elements should be kept the same.

        Since it is impossible to change the length of the array in some languages,
        you must instead have the result be placed in the first part of the array nums.
        More formally, if there are k elements after removing the duplicates,
        then the first k elements of num should hold the final result.
        It does not matter what you leave beyond the first k elements.

        Return k after placing the final result in the first k slots of nums.

        Do not allocate extra space for another array.
        You must do this by modifying the input array in-place with O(1) extra memory.
        """
        # Two pointers approach, with the help of dict
        twice_dict = {nums[0]: 1}  # dict of elements appearing at most twice
        left = 1  # pointer to the tail of elements appearing at most twice, on the left side of the original array
        right = 1  # pointer for traversing the array

        while right < len(nums):
            twice_dict[nums[right]] = twice_dict.get(nums[right], 0) + 1
            if twice_dict[nums[right]] <= 2:
                nums[left] = nums[right]
                left += 1

            right += 1

        return left

    @staticmethod
    def remove_duplicates_from_sorted_array_II_2(nums: List[int]) -> int:
        # optimized two pointers approach, by using the given condition that the array is 'sorted'
        left = 1  # pointer to the tail of unique elements, which are placed on the left side of the original array
        right = 1  # pointer for traversing the array
        count = 1  # counter of appearing times of unique elements

        while right < len(nums):
            if nums[right] == nums[right - 1]:
                if count < 2:
                    nums[left] = nums[right]
                    left += 1

                count += 1

            else:
                nums[left] = nums[right]
                left += 1
                count = 1

            right += 1

        return left

    @staticmethod
    def remove_duplicates_from_sorted_array_II_3(nums: List[int]) -> int:
        # further optimized version based on the function of 'remove_duplicates_from_sorted_array_II_2'
        size = len(nums)
        if size <= 2:
            return size

        slow, fast = 2, 2
        while fast < size:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow


    @staticmethod
    def remove_duplicates_from_sorted_array_1(nums: List[int]) -> int:
        """
        Leet Code # 26

        Given an integer array nums sorted in non-decreasing order,
        remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same.
        Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
            - Change the array nums such that the first k elements of nums contain the unique elements
            in the order they were present in nums initially.
            The remaining elements of nums are not important as well as the size of nums.
            - Return k.
        """
        # Two pointers approach, with the help of set
        unique_set = set()  # set of unique elements
        unique_set.add(nums[0])
        left = 1    # pointer to the tail of unique elements, which are placed on the left side of the original array
        right = 1   # pointer for traversing the array

        while right < len(nums):
            if nums[right] not in unique_set:
                unique_set.add(nums[right])
                nums[left] = nums[right]
                left += 1

            right += 1

        return left

    @staticmethod
    def remove_duplicates_from_sorted_array_2(nums: List[int]) -> int:
        # optimized two pointers approach, by using the given condition that the array is 'sorted'
        left = 1    # pointer to the tail of unique elements, which are placed on the left side of the original array
        right = 1   # pointer for traversing the array

        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

            right += 1

        return left

    @staticmethod
    def remove_element_1(nums: List[int], val: int) -> int:
        """
        Leet Code # 27

        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
            - Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
            The remaining elements of nums are not important as well as the size of nums.
            - Return k.
        """
        # Two pointers approach
        left = 0        # pointer to the tail of the non-target element

        # another point 'i' for traversing the array sequentially
        for i, num in enumerate(nums):
            if num != val:
                nums[left] = num
                left += 1

        return left

    @staticmethod
    def remove_element_2(nums: List[int], val: int) -> int:
        # Optimized two pointers approach
        left, right = 0, len(nums) - 1      # two pointers to the head and tail of the array

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return left

    @staticmethod
    def merge_sorted_array_1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Leet code # 88

        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        # merge and sort
        # Time complexity: O((m + n) * log(m + n))
        # Space complexity: O(1)
        nums1[m:] = nums2[:]
        nums1.sort()

    @staticmethod
    def merge_sorted_array_2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Use two pointers, and traverse the arrays from left to right
        # Time complexity: O(m + n)
        # Space complexity: O(m + n)
        nums1_copy = nums1[:]
        p1, p2 = 0, 0  # two pointer point to the arrays nums1_copy and nums2 respectively
        i = 0  # pointer to nums1
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1

            i += 1

        while p1 < m:
            nums1[i] = nums1_copy[p1]
            i += 1
            p1 += 1

        while p2 < n:
            nums1[i] = nums2[p2]
            i += 1
            p2 += 1

    @staticmethod
    def merge_sorted_array_3(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # rewrite the function of merge_sorted_array2 in a more pythonic way
        nums1_copy = nums1[:]
        p1, p2 = 0, 0
        i = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1

            i += 1

        if p1 < m:
            nums1[i:] = nums1_copy[p1:]

        if p2 < n:
            nums1[i:] = nums2[p2:]

    @staticmethod
    def merge_sorted_array_4(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Use two pointers, but traverse the arrays from right to left, so no need for extra space
        # https://leetcode.cn/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/
        # Time complexity: O(m + n)
        # Space complexity: O(1)
        p1 = m - 1              # pointer to the last non-zero element of nums1
        p2 = n - 1              # pointer to the end of nums2
        p = len(nums1) - 1      # pointer to the end of nums1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1

        if p1 >= 0:
            nums1[:p+1] = nums1[:p1+1]

        if p2 >= 0:
            nums1[:p+1] = nums2[:p2+1]
