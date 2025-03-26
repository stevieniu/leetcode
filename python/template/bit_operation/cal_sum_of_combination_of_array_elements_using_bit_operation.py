# calculate the sum of all combinations of the arr
# arr[0] + arr[1], arr[0] + arr[2], .., arr[0] + arr[2] + arr[4],...
arr = [3, 2, 4]
n = len(arr)
sum_arr = [0] * (1 << n)

# states are 000, 001, 010, 011, 100, 101, 110, 111 | 1 means consider this position, 0 means no consider this position
for state in range(1 << n):
    sum = 0
    for i in range(n):
        if (state >> i & 1):
            sum += arr[i]
        sum_arr[state] = sum
print(sum_arr)
