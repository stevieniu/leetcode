"""
170.  Two Sum III - Data structure design

https://leetcode.com/problems/two-sum-iii-data-structure-design/description/

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.


Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false


Constraints:

-105 <= number <= 105
-231 <= value <= 231 - 1
At most 104 calls will be made to add and find.

"""


class TwoSum:

    # def __init__(self):
    #     self.arr = []
    #     self.is_sorted = False

    # def add(self, number: int) -> None:
    #     self.arr.append(number)
    #     self.is_sorted = False

    # def find(self, value: int) -> bool:
    #     if not self.is_sorted:
    #         self.arr.sort()
    #         self.is_sorted = True
    #     l, r = 0, len(self.arr) - 1
    #     while l < r:
    #         if self.arr[l] + self.arr[r] == value:
    #             return True
    #         elif self.arr[l] + self.arr[r] < value:
    #             l += 1
    #         else: r -= 1
    #     return False

    def __init__(self):
        self.nums = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.nums.sort()

        l, r = 0, len(self.nums) - 1
        while l < r:
            if self.nums[l] + self.nums[r] == value:
                return True
            elif self.nums[l] + self.nums[r] > value:
                r -= 1
            else:
                l += 1
        return False
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)