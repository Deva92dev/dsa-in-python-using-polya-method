from itertools import islice


def shortest_path(arr, target):
    left = 0
    min_length = float("inf")
    window_sum = sum(islice(arr, 0))

    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum = window_sum - arr[left]
            left += 1

    return min_length if min_length != float("inf") else 0
