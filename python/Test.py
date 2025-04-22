def partition(arr, val):
    l, r = 0, len(arr) - 1
    i = 0
    while i <= r:
        if arr[i] > val:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        elif arr[i] < val:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i += 1
        else:
            i += 1
    return arr

arr = [3, 2, 1, 5, 3, 6, 4, 5, -1 , 0, 3, 3]
val = 3
print(partition(arr, val))

#          l
# 2, 1, 0, 3, 3, 3, 3, -1, 5 , 4, 6, 5
#                      i
#                       r
