"""
Author: Amit Pratap

Given an array arr[] consisting of only 0s, 1s, and 2s. The task is to sort the array, i.e., 
put all 0s first, then all 1s and all 2s in last.

This problem is the same as the famous “Dutch National Flag problem”. The problem was proposed 
by Edsger Dijkstra. The problem is as follows:
    Given n balls of colour red, white or blue arranged in a line in random order. You have to arrange all the 
    balls such that the balls with the same colours are adjacent with the order of the balls, with the order 
    of the colours being red, white and blue (i.e., all red coloured balls 
    come first then the white coloured balls and then the blue coloured balls). 

    Input: arr[] = {0, 1, 2, 0, 1, 2}
    Output: {0, 0, 1, 1, 2, 2}
    Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
"""

def DNFAlgo(arr):
    # start by setting the low, high and mid
    low = 0
    mid = 0
    high = len(arr)-1

    while mid <= high:
        # print(arr, low, mid, high, arr[mid])
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        elif arr[mid] == 1:
            mid += 1
    
        
    return arr

if __name__=="__main__":
    arr = [0, 1, 2, 0, 1, 2, 0, 0, 0, 1,2,1,2,1]

    new_arr = DNFAlgo(arr)
    print(f'The sorted array: {new_arr}')