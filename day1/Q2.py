'''
MONOTONIC ARRAY

Question
An array is monotonic if its either monotone increasing or monotone decreasing. An array is monotone
increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing
if all its elements from left to right are non-increasing. Given an integer array return true if 
the given array is monotonic, or false otherwise

Clarifying Questions

Is an empty array monotonic?
A: Yes

Is an array with only 1 integer monotonic?
A: Yes

TEST CASES

[1,2,3] Non decreasing, so its monotonic (true)
[3,2,1] Non increasing, also montonic
[1,2,2] Non decreasing, also monotonic
[3,3,3] true
[7] true
[] true
[2,2,3,1] false

Method and Big O analysis

non increasing
    array[i] >= array[i+1]
non decreasing
    array[i] <= array[i+1]
Time = O(n)
Space = 0(n)


'''

array = [1,2,3]

def monotonic_array(array):
    n = len(array)
    if n == 0: return True
    first = array[0]
    last = array[n-1]
    if first>last:
        #MD or array is not monotonic
        for k in range(n-1):
            if array[k] < array[k+1]: return False
    elif first == last:
        for k in range(n-1):
            if array[k] != array[k+1]: return False
        #M - all alues are equal
    else:
        #first < last
        #MI or arrays is not monotonic
        for k in range(n-1):
            if array[k] > array[k+1]: return False
    return True

r = monotonic_array(array)
print(r)