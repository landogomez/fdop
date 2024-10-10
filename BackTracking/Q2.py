'''
Permutations 2
Given a collection of numbers, nums, that might contain duplicates, return all possible unique 
permutations in any order.


Approach

Test case
i=0
j = 0 to 2
                  0 1 2
                 [1,1,2]
          [1,1,2]       [1,1,2]*     [2,1,1]
create a hashtable          avoid * 
and add 1 to it         before this, chech if 1 is in hash


Pseudocode

function perm(){
    if i = len-1 --> add to result
    hash = {}
    for j = i to len-1{
        if nums[j] not in hash, insert it
        swap nums[i] & nums[j]
        perm(i+1)
        swap nums[i] & nums[j] --> backtracking
    }

    S = O(n)
    T = O(nxn!)
} 
'''

def permuteUnique(nums):
    res = []
    def helper(i):
        #base case
        if i == len(nums)-1:
            res.append(nums[:])
            return
        #recursive case
        hash = {}
        for j in range(i,len(nums)):
            if nums[j] not in hash:
                hash[nums[j]] = True
                nums[i],nums[j] = nums[j],nums[i]
                helper(i+1)
                nums[i],nums[j] = nums[j],nums[i]
    helper(0)
    return res

print(permuteUnique([1,1,2]))