"""
Author: Amit Pratap

Given an array arr[] of n integers and a target value, the task is to find whether 
there is a pair of elements in the array whose sum is equal to target. This problem 
is a variation of 2Sum problem.               
"""

def TwoSum(arr, target):

    # first sort the data
    arr.sort()
    n = len(arr)

    # now define left and right values
    left = 0
    right = n-1

    # now add the left and right values to get the result
    while True:
        tmp_sum = arr[left] + arr[right]

        if left == right:
            return None, None
        elif tmp_sum > target:
            right -= 1
        elif tmp_sum < target:
            left += 1
        elif tmp_sum == target:
            return arr[left], arr[right]
    
    

if __name__=="__main__":
    arr = [1,8,2,5,3,6,7]
    target_sum = 15 

    num1, num2 = TwoSum(arr, target_sum)
    if num1 is not None:
        print(f"The numbers {num1} and {num2} sum to {target_sum}")
    else:
        print(f'There are no two numbers that add upto {target_sum}')

