from itertools import islice


def max_sum_sub_array(arr, k):
    if len(arr) < k:
        return []

    window_sum = sum(islice(arr, k))
    highest = window_sum

    # Loop from index k to the end of the array
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > highest:
            highest = window_sum
        else:
            continue

    return highest
