'''
You are given an array of integers in which each subsequent value is not less than the previous value.
Write a function that takes this array as an input and returns a new array with the square of each number
sorted in ascending order.
'''

#Clarifying Questions

'''
Are all numbers positive?
A: No, there can be negative values and 0 also

Are all the Integeres distinct?
A: Not necessariliy

Can an empty array of Integeres be given as an input?
A: Yes, return an empty array in this case
'''

# Test Cases

'''
Different inputs, expected outputs

input = [1,3,5]
output = [1,9,25]

input = [0,5,6]
output = [0,25,36]

input = [-4,-2,0,1,3]
output = [0,1,4,9,16]
'''

# Method 1 Brute Force Method

'''
input = [-3,1,2,7]
-> Square each element and print in a new array 
Time = O(n)
[9,1,4,49]

-> Sort this array
Time = O(nlogn)
Space = O(n), creating a new sorted array of n length
[1,4,9,49]

Time = O(nlogn)
Space = O(n)
'''
array = [-3,1,2,7]


def sorted_squared(array):
    n = len(array)
    res = [0]*n
    for i in range(n):
        res[i] = array[i]**2
    res.sort()
    return res


r = sorted_squared(array)
print(r) 

# Method 2 
'''
Make us of the fact that given Array is sorted in ascending order
[-3,1,2,7]

-> initialize an empty output array with the same length as input
[0,0,0,0]

the square of each number icresease toward the extremes of the line <-----0------>
Loking at 2 extremes we can visualize that both of them will be greatest values when we squared it
-3 or 7 one among these 2 has to be the largest
[-3*,1,2,*7] 
9 < 49
[0,0,0,49] 

so we move the pointer to the left
[-3*,1,2*,7]
9>4
[0,0,9,49]
we move the pointer
[-3,1*,2*,7]
1 < 2
[0,4,9,49]

[-3,1**,2,7]
Both pointers are on the same number so we fill the last spot with that value
[1,4,9,49]

Time complexity = O(n) We only travel the array once
Space = O(n)
'''

print("Method 2")

def sorted_squared2(array):
    n = len(array)
    i,j =0,n-1     # i first index and j is going to be the last index of the array
    res = [0]*n # Create a new array
    for k in reversed(range(n)):
        if array[i]**2>array[j]**2:
            res[k] = array[i]**2
            i+=1
        else:
            res[k] = array[j]**2
            j-=1
    return res

print(sorted_squared2(array))
    
    
