""""
Author: Amit Pratap

Flipbits using Kadane algorithm. this is the maximum number of flips
of 0 to 1 
"""
import sys

def conv_num(num):
    if num =='0':
        return 1
    else:
        return -1

def find_largest(arr):

    ans = 0

    for i in arr:
        if i == '1':
            ans += 1

    max_sum = -sys.maxsize + 1
    curr_sum = 0
    start = 0
    end = 0
    no_loops = 0

    n = len(arr)
    while end < n:
        while curr_sum < 0:
            curr_sum -= conv_num(arr[start])
            start += 1
            # no_loops += 1
        curr_sum += conv_num(arr[end])
        end += 1

        max_sum = max(curr_sum, max_sum)
        # no_loops += 1
    
    return max_sum + ans, start, end, no_loops


if __name__ == '__main__':
    arr = '001111000'

    max_sum, start, _, no_loops = find_largest(arr)

    print(f"The largest sum is: {max_sum} | start: {start} | loops: {no_loops}")