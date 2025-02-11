""""
Author: Amit Pratap

This program is top calculate the largest sum of the consequtive
sequence of elements in an array using Kadane algorithm.
"""
import sys

def find_largest(arr):
    max_sum = -sys.maxsize + 1
    curr_sum = 0
    start = 0
    end = 0
    no_loops = 0

    n = len(arr)
    while end < n:
        while curr_sum < 0:
            curr_sum -= arr[start]
            start += 1
            # no_loops += 1
        curr_sum += arr[end]
        end += 1

        max_sum = max(curr_sum, max_sum)
        # no_loops += 1
    
    return max_sum, start, end, no_loops


if __name__ == '__main__':
    arr = [1, 2, -1, 3, -10, 1, 10, 11, -100, 1, 1, 1, 200]

    max_sum, start, _, no_loops = find_largest(arr)

    print(f"The largest sum is: {max_sum} | start: {start} | loops: {no_loops}")