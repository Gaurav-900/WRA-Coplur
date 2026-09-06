def longest_subarray(arr, k):
    seen = {}
    total = 0
    best = 0

    for i, num in enumerate(arr):
        total += num

        if total == k:
            best = i + 1

        diff = total - k
        if diff in seen:
            best = max(best, i - seen[diff])

        if total not in seen:
            seen[total] = i

    return best


if __name__ == "__main__":
    arr1 = [10, 5, 2, 7, 1, 9]
    k1 = 15
    print("Example 1:", longest_subarray(arr1, k1))  # 4

    arr2 = [-5, 8, -2, 4, 3, -8, 6]
    k2 = 5
    print("Example 2:", longest_subarray(arr2, k2))  # 5