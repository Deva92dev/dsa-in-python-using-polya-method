#  The Problem:

# You are given an array of integers that is already sorted in ascending order. You are also given a target integer.Your goal is to find exactly three distinct numbers in the array that add up to the exact target value, and return their indices.

# Desired Outcome Example:
# Input: arr = [1, 2, 4, 5, 8, 12], target = 11
# Output: [0, 1, 4] (Because indices 0, 1, and 4 hold the values 1, 2, and 8, and 1 + 2 + 8 = 11)

# Strict Constraints:

# Space Complexity: Strictly $O(1)$. No hash tables, no auxiliary arrays, no storage tracking systems. Only independent pointer variables.

# Time Complexity: Strictly $O(N^2)$. You cannot use three nested loops ($O(N^3)$ is a hard failure).

# Guarantees: Every test case will contain exactly one unique combination of three elements that solves the problem. You cannot use the same index multiple times to form the sum.


def three_sum_sorted(arr, target):
    for i in range(len(arr) - 2):
        second_pointer = i + 1
        third_pointer = len(arr) - 1

        while second_pointer != third_pointer:
            total = arr[i] + arr[second_pointer] + arr[third_pointer]

            if total < target:
                second_pointer += 1

            elif total > target:
                third_pointer -= 1

            elif total == target:
                return [i, second_pointer, third_pointer]
