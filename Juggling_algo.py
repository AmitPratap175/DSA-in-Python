"""
Author: Amit Pratap

Given an array arr[], the task is to rotate the array by d positions to the left using juggling algorithm.

Examples:

    Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
    Output: {3, 4, 5, 6, 1, 2}
    Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, 
                    arr[] becomes {3, 4, 5, 6, 1, 2}

    Input: arr[] = {1, 2, 3}, d = 4
    Output: {2, 3, 1}
    Explanation: The array is rotated as follows: 

        After first left rotation, arr[] = {2, 3, 1} 
        After second left rotation, arr[] = {3, 1, 2}
        After third left rotation, arr[] = {1, 2, 3}
        After fourth left rotation, arr[] = {2, 3, 1} 
"""
from math import gcd

def JuggleAlgo(arr, d):
    n = len(arr)
    no_cycles = gcd(n,d)

    for i in range(no_cycles):
        startEle = arr[i]
        currIdx = i
        for j in range(n//d-1):
            nextIdx = (i + (j+1) * d) % n
            # print(nextIdx, currIdx)                
            
            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx
        arr[currIdx] = startEle

    return arr
            

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 3

    new_arr = JuggleAlgo(arr, d)
    print(f" The rotated array is : {new_arr}")

