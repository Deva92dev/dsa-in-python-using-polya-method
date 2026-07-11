# The Problem:You are given an array of integers. Some of these integers are 0.Your goal is to move all the 0s to the very end of the array, while maintaining the exact relative order of all the non-zero elements.

# If memory starts as: [0, 1, 0, 3, 12]
# Memory must end as: [1, 3, 12, 0, 0]

# Strict Constraints:
# Space Complexity: Strictly $O(1)$. (Definition: You may use a few individual variables for pointers or temporary holds, but you cannot create a second array/list. You must mutate the existing array in-place).

# Operations: You must minimize the total number of operations.


def move_zeroes(arr):
    first_pointer = 0  # placed at index not values
    second_pointer = 1

    if len(arr) == 1:
        return arr

    while second_pointer <= len(arr) - 1:
        temp = arr[first_pointer]
        if arr[first_pointer] != 0 and arr[second_pointer] != 0:
            first_pointer += 1
            second_pointer += 1

        elif arr[first_pointer] != 0 and arr[second_pointer] == 0:
            first_pointer += 1
            second_pointer += 1

        elif arr[first_pointer] == 0 and arr[second_pointer] == 0:
            second_pointer += 1

        elif arr[first_pointer] == 0 and arr[second_pointer] != 0:
            # assign the reference of first pointer value to second pointer value
            arr[first_pointer] = arr[second_pointer]
            arr[second_pointer] = temp

            first_pointer += 1
            second_pointer += 1

    return arr
