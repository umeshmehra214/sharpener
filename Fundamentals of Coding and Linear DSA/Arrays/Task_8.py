# Subarrays :----->

# Task details

# Question :- write the code to print all the subarrays possible. Note - print in the similar way as given here.

# Input:-

# [1,2,3,4,5]

# Output:-

# 1
# 12
# 123
# 1234
# 12345
# 2
# 23
# 234
# 2345
# 3
# 34
# 345
# 4
# 45
# 5


#========== User's Code Starts Here ==========
```python
def print_subarray(arr, length):
  n = len(arr)
  # Generate all subarrays
  for i in range(n):
    for j in range(i, n):
      subarray = arr[i:j+1]
      print(''.join(map(str, subarray)))

def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print_subarray(arr, n)
    
main()

    
#========== User's Code Ends Here ==========
