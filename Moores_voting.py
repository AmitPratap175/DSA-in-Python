"""
Author: Amit Pratap

The Boyer-Moore voting algorithm is one of the popular optimal algorithms which is used 
to find the majority element among the given elements that have more than N/ 2 occurrences.
This works perfectly fine for finding the majority element which takes 2 traversals over the 
given elements, which works in O(N) time complexity and O(1) space complexity.

Let us see the algorithm and intuition behind its working, by taking an example 

Input :{1,1,1,1,2,3,5}
Output : 1
Explanation : 1 occurs more than 3 times.
Input : {1,2,3}
Output : -1

"""

def VoteMoore(arr):
    num = -1
    vote = 0
    n = len(arr)

    for i in range(n):
        if vote == 0:
            num = arr[i]
            vote = 1
        elif arr[i] == num:
            vote += 1
        elif arr[i] != num:
            vote -= 1
    
    count = 0
    
    # Checking if majority candidate occurs more than n/2
    # times
    for i in range(n):
        if (arr[i] == num):
            count += 1
            
    if (count > n // 2):
        return num
    else:
        return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,67,1,2,1,1,1,1,1]

    num = VoteMoore(arr)
    print(f"The most ocurring element in {arr} is : {num}")