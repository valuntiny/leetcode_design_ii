'''
Requirement:
Design a data structure that supports all following operations in average O(1) time:
    1. insert(val): Inserts an item val to the set if not already present.
    2. remove(val): Removes an item val from the set if present.
    3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Solution:
create two variables:
    val [] for storing the values
    pos {} for storing the position info using hashmap: key = val, value = position
'''


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.val.append(val)
            self.pos[val] = len(self.val) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            self.val.remove(val)
            self.pos.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.val[random.randint(0, len(self.val)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()