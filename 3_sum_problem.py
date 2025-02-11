"""
Author: Amit Pratap

Given an array arr[] of n integers and a target value, the task is to find whether 
there are 3 elements in the array whose sum is equal to target. This problem 
is a variation of 3Sum problem.               
"""

def ThreeSum(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(n - 2):  # Iterate up to n-2 to leave space for two more numbers
        left, right = i + 1, n - 1  # Two-pointer approach

        while left < right:
            tmp_sum = arr[i] + arr[left] + arr[right]

            if tmp_sum == target:
                return arr[i], arr[left], arr[right]
            elif tmp_sum < target:
                left += 1
            else:
                right -= 1

    return None, None, None


if __name__ == "__main__":
    arr = [11, 4, 45, 6, 10, 8, 1,5]
    target_sum = 22

    num1, num2, num3 = ThreeSum(arr, target_sum)
    if num1 is not None:
        print(f"The numbers {num1}, {num2}, and {num3} sum to {target_sum}")
    else:
        print(f'There are no three numbers that add up to {target_sum}')
