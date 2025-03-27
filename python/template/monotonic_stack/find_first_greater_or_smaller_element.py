# arr[a1, a2, a3...] find first element that is greater than current element, for each element in the array
# we use decreasing monotonic stack to implement
# if use native way, to compare current num with every number following, time complexity is O(n^2)
# here is what we do:
# create a array nge = [-1] * len(numbers), store the first index whose number is greater than the current number, intialize with -1 for all positions
# e.g. nge[2] = 4, means : the first index whose number is greater or equal to the number at index 2, is at index 4
# use monotonic decreasing stack, if the stack is empty, simply push the current index to the stack
# if the stack is not empty and the current number is greater than the number whose index is the top of the stack,
# then, the current index is the first index whose number is greater than the number whose index is the top of the stack
# i.e. set  nge[stack[-1]] = curr_idx
# then pop stack, because already set this index, no need anymore, and push curr_idx to the stack
# in this way, the time complexity is O(n)
def find_first_greater_element_idx(arr):
    stack_desc = [] # store index for the current index
    nge = [-1] * len(arr)
    for i, num in enumerate(arr):
        while stack_desc and num > arr[stack_desc[-1]]:
            nge[stack_desc.pop()] = i
        stack_desc.append(i)
    print(nge)

# similar logic for find_first_greater_element_idx, instead of using descreasing monotoic stack, we use increasing monotonic stack this time
def find_first_smaller_element_idx(arr):
    stack_asc = [] # store index for the current index
    lne = [-1] * len(arr)
    for i, num in enumerate(arr):
        while stack_asc and num < arr[stack_asc[-1]]:
            lne[stack_asc.pop()] = i
        stack_asc.append(i)
    print(lne)
nums = [3,2,4,4,1]
find_first_greater_element_idx(nums)
find_first_smaller_element_idx(nums)