nums = [3,2,4,4,1]
stack_inc, stack_dec = [], [] # store indices before current index i
nge, nle = [-1] * len(nums), [-1] * len(nums)
for i, num in enumerate(nums):
    while stack_dec and num >= nums[stack_dec[-1]]:
        nge[stack_dec.pop()] = i
    stack_dec.append(i)
print(nge)

# [ 2 ]
# [2, 2, -1, -1, -1]