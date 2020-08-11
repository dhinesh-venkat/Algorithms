def linear(x,arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

x = 11
arr = [4,12,7,20,11,83,29,44,28]
print(linear(x,arr))

# Running time is O(n)