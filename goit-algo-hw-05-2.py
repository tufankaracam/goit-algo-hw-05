def binary_search_with_upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]
        else:
            return (iterations, arr[mid])

    if low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)


arr = [2, 3, 4, 10, 40]

result = binary_search_with_upper_bound(arr, 10)
print(f"Iterasyon Count: {result[0]}, Upper Bound: {result[1]}")

result = binary_search_with_upper_bound(arr, 8)
print(f"Iterasyon Count: {result[0]}, Upper Bound: {result[1]}")
