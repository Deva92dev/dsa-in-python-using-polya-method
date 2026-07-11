#  The Problem:

# You are given an array of integers that is already sorted in ascending order (from smallest to largest). You are also given a target integer.Your goal is to find exactly two distinct numbers in the array that add up to the target value, and return their indices.

# Example of the desired outcome:

# Input: arr = [2, 7, 11, 15], target = 9
# Output: [0, 1] (Because the value at index 0 is 2, the value at index 1 is 7, and 2 + 7 = 9)

# Strict Constraints:
# Space Complexity: Strictly $O(1)$. You cannot create a hash map, a dictionary, or a second array to keep track of numbers. You may only use independent pointer variables.

# Time Complexity: Strictly $O(N)$. You cannot use nested loops (no checking every number against every other number). You must find the answer in a single, fluid traversal of the data.

# Guarantees: Every test case will have exactly one valid solution. You cannot use the same element twice.


def two_sum_sorted(arr, target):
    first_pointer = 0
    second_pointer = len(arr) - 1

    while first_pointer != second_pointer:
        current_sum = arr[first_pointer] + arr[second_pointer]
        if current_sum > target:
            second_pointer -= 1

        elif current_sum < target:
            first_pointer += 1

        elif current_sum == target:
            return [first_pointer, second_pointer]
