import random
class RandomizedSet:

    def __init__(self):
        self.cache = {}  # {number : index in the arr}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        self.cache[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache: return False
        # [1, 2, 3, 0 ]  => [1, 0, 3] . pop 0
        # cache = {1: 0, 2: 1, 3: 2, 0: 3}
        # remove 2
        idx = self.cache[val]
        del self.cache[val]
        self.arr[idx] = self.arr[-1]  # assign last value of the arr to the position to be deleted
        self.cache[self.arr[-1]] = idx  # update cache, poiting last value to the position to be deletd
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

obj = RandomizedSet()
obj.insert(0)
obj.remove(0)
obj.insert(0)