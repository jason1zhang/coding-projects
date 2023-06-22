import sys
from typing import List

class LCArray:
    @staticmethod
    def length_of_last_word(s: str) -> int:
        """
        Leet Code # 58
        Given a string s consisting of words and spaces, return the length of the last word in the string.

        A word is a maximal substring consisting of non-space characters only.
        """
        length = 0
        for i in reversed(range(len(s))):
            if s[i] == ' ':
                if length == 0:
                    continue
                else:
                    break

            length += 1

        return length

    @staticmethod
    def int_to_roman(num: int) -> str:
        """
        Leet Code # 12
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
        which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four
        is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it
        making four. The same principle applies to the number nine, which is written as IX. There are six instances
        where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given an integer, convert it to a roman numeral.
        """
        mapping = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman = list()
        for val, symbol in mapping:
            while num >= val:
                num -= val
                roman.append(symbol)

            if num == 0:
                break

        return "".join(roman)

    @staticmethod
    def roman_to_int(s: str) -> int:
        """
        Leet Code # 13 Roman to Integer

        https://leetcode.cn/studyplan/top-interview-150/

        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        For example, 2 is written as II in Roman numeral, just two ones added together.
        12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four
        is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it
        making four. The same principle applies to the number nine, which is written as IX. There are six instances
        where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.
        """
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        answer, n = 0, len(s)
        for i, ch in enumerate(s):
            val = mapping[ch]
            if i < n - 1 and val < mapping[s[i + 1]]:
                answer -= val   # if current value smaller than the next one, subtract current value from the answer
            else:
                answer += val

        return answer

    @staticmethod
    def can_complete_circuit_2(gas: List[int], cost: List[int]) -> int:
        """
        Second solution with graph idea
        """
        n, spare, min_spare, min_index = len(gas), 0, sys.maxsize, 0
        for i in range(n):
            spare += (gas[i] - cost[i])
            if spare < min_spare:
                min_spare = spare
                min_index = i

        if spare < 0:
            return -1
        elif min_spare >= 0:
            return 0
        else:
            return (min_index + 1) % n

    @staticmethod
    def can_complete_circuit_1(gas: List[int], cost: List[int]) -> int:
        """
        Leet code #134 Gas Station

        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
        to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
        the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed
        to be unique
        """
        n, i = len(gas), 0
        while i < n:
            sum_gas, sum_cost, count = 0, 0, 0
            while count < n:
                j = (i + count) % n
                sum_gas += gas[j]
                sum_cost += cost[j]
                if sum_cost > sum_gas:
                    break

                count += 1

            if count == n:
                return i
            else:
                i += (count + 1)

        return -1


    @staticmethod
    def product_except_self_2(nums: List[int]) -> List[int]:
        """
        Space optimized version
        """
        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        right = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer

    @staticmethod
    def product_except_self_1(nums: List[int]) -> List[int]:
        """
        Leet Code # 238 Product of Array Except Self
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of
        all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        length = len(nums)

        # left_product is the product of all the left elements for an array element,
        # and right_product is the product of all the right elements for that element.
        left_product, right_product, answer = [0] * length, [0] * length, [0] * length

        left_product[0] = 1  # for the first element, its left_product is 1
        for i in range(1, length):
            left_product[i] = nums[i - 1] * left_product[i - 1]

        right_product[length - 1] = 1  # for the last element, its right_product is 1
        for i in reversed(range(length - 1)):
            right_product[i] = nums[i + 1] * right_product[i + 1]

        for i in range(length):
            answer[i] = left_product[i] * right_product[i]

        return answer

    @staticmethod
    def h_index(citations: List[int]) -> int:
        """
        Leet Code # 274
        
        Given an array of integers citations where citations[i] is the number of citations a researcher
        received for their ith paper, return the researcher's h-index.

        According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of
        h such that the given researcher has published at least h papers that have each been cited at least h times.
        """
        # sort the array reversely, then traverse the sorted array and calculate the h-index
        reverse_sorted_citations = sorted(citations, reverse=True)

        h, i, n = 0, 0, len(citations)
        while i < n and reverse_sorted_citations[i] > h:
            h += 1
            i += 1

        return h

    @staticmethod
    def jump(nums: List[int]) -> int:
        """
        Leet code # 45

        You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

        Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
        if you are at nums[i], you can jump to any nums[i + j] where:
            - 0 <= j <= nums[i] and
            - i + j < n

        Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can
        reach nums[n - 1].
        """
        # Greedy algorithm
        n, max_pos, end, step = len(nums), 0, 0, 0
        for i in range(n - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    end = max_pos
                    step += 1

        return step


    @staticmethod
    def can_jump_1(nums: List[int]) -> bool:
        """
        Leet code # 55

        You are given an integer array nums. You are initially positioned at the array's first index,
        and each element in the array represents your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.
        """
        # Greedy algorithm
        right_most, size = 0, len(nums)
        for i in range(size):
            if i > right_most:
                return False
            right_most = max(i + nums[i], right_most)

        return True

    @staticmethod
    def can_jump_2(nums: List[int]) -> bool:
        # Greedy algorithm 2
        right_most, size = 0, len(nums)
        for i in range(size):
            if i <= right_most:
                right_most = max(i + nums[i], right_most)
                if right_most >= (size - 1):
                    return True

        return False

    @staticmethod
    def can_jump_3(nums: List[int]) -> bool:
        # Start from the tail, and traverse backwards,but this approach is slightly worse than approach 2 above
        left_most, size = len(nums) - 1, len(nums)
        for i in range(size - 2, -1, -1):
            if i + nums[i] >= left_most:
                left_most = i

        return left_most == 0

    @staticmethod
    def max_profit_II(prices: List[int]) -> int:
        """
        Leet code # 122

        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of
        the stock at any time. However, you can buy it then immediately sell it on the same day.

        Find and return the maximum profit you can achieve.
        """
        # Greedy algorithm
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i] - prices[i - 1])

        return max_profit

    @staticmethod
    def max_profit_1(prices: List[int]) -> int:
        """
        Leet Code # 121

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
        in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        """
        # brute-force approach
        size = len(prices)
        profit = 0
        for i in range(size):
            for j in range(i + 1, size):
                profit = max(profit, prices[j] - prices[i])

        return profit

    @staticmethod
    def max_profit_2(prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = max(prices)
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif (price - min_price) > max_profit:
                max_profit = price - min_price

        return max_profit

    @staticmethod
    def rotate_array_1(nums: List[int], k: int) -> None:
        """
        Leet code # 189
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

        Do not return anything, modify nums in-place instead.
        """
        # Use one extra list
        size = len(nums)
        nums_copy = nums.copy()
        for i, num in enumerate(nums):
            nums_copy[(i + k) % size] = nums[i]

        nums[:] = nums_copy[:]

    @staticmethod
    def rotate_array_2(nums: List[int], k: int) -> None:
        # Rotate the array 3 times
        # Note: be careful with the indexing when reversing
        size = len(nums)
        k %= size
        if k == 0:
            return

        nums[:] = nums[::-1]
        nums[0: k] = nums[k - 1::-1]
        nums[k: size] = nums[size - 1: k - 1: -1]


    @staticmethod
    def majority_element_1(nums: List[int]) -> int:
        """
        Leet code # 169

        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.
        """
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        max_key, max_value = 0, 0

        for key, value in counter.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key

    @staticmethod
    def majority_element_2(nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return max(counter.keys(), key=counter.get)

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
