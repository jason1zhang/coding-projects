import random


class RandomizedSet:
    """
    You must implement the functions of the class such that each function works in average O(1) time complexity.
    """

    def __init__(self):
        self.nums = []  # an array to store the values
        self.indices = {}  # a dict {value: index} to store the indices of the inserted values

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        """
        if val in self.indices:
            return False

        self.indices[val] = len(self.nums)
        self.nums.append(val)  # insert at the end of the array
        return True

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        """
        if val not in self.indices:
            return False

        idx = self.indices[val]
        self.nums[idx] = self.nums[-1]  # move the last value to the position where the val to be removed
        self.indices[self.nums[idx]] = idx
        self.nums.pop()
        del self.indices[val]
        return True

    def get_random(self) -> int:
        """
        Returns a random element from the current set of elements (it's guaranteed that at least one element exists
        when this method is called). Each element must have the same probability of being returned.
        """
        return self.nums[int(random.random() * len(self.nums))]
