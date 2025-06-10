"""
1570. Dot Product of Two Sparse Vectors
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?



Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6


Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
"""
from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.tuples = [] # (index, number)  store number which is not 0
        for i, num in enumerate(nums):
            self.tuples.append((i, num))

    # Return the dotProduct of two sparse vectors
    # O(n)
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        i = j = 0
        while i < len(self.tuples) and j < len(vec.tuples):
            if self.tuples[i][0] == vec.tuples[j][0]: # the same index, do multiplication
                product += self.tuples[i][1] * vec.tuples[j][1]
                i += 1
                j += 1
            elif self.tuples[i][0] < vec.tuples[j][0]:
                i += 1
            else:
                j += 1

        return product

    # O(log(n))
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for i in range(len(self.tuples)):
            j = self.binary_search(0, len(vec.tuples) - 1, vec.tuples, i)
            if j != -1:
                product += self.tuples[i][1] * vec.tuples[i][1]

        return product

    def binary_search(self, l, r, nums, target_idx):  # nums: list of tuples (id, num)
        while l <= r:
            m = (l + r) // 2
            if nums[m][0] == target_idx:
                return target_idx
            elif nums[m][0] < target_idx:
                l = m + 1
            else:
                r = m - 1
        return -1

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# 0: [1, 0]
# 1: [0, 3]
# 2: [0, 0]
# 3: [2, 4]
# 4: [3, 0]