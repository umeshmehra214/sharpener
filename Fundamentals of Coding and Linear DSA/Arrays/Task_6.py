# Minimum Element In An Array :----->

# Task details

# Complete the function to find the minimum in the array and return it

# Input :- Array and the length of the array

# [5,6,2,9,-2] , 5


# Output  :----->    -2

# Question :- Write a program to return the minimum element in the array.


#========== User's Code Starts Here ==========

def find_minimum(arr, length):
    min = 999999
    for i in arr:
        if i < min:
            min = i
    return min

  
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_minimum(arr, n))
    
main()

    
#========== User's Code Ends Here ==========
