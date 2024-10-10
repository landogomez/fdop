'''
Identify Backtracking 

- If a problem requieres every possible path
- There are multiple solutions and you want all of them
- NOT for optimisation problems


Question

Given an array nums of distinct integers, return all the possible permutations. You can return the 
answer in any order

Ex. [1,2,3]
-> [1,2,3]
-> [1,3,2]
-> [2,1,3]
-> [2,3,1]
->  [3,1,2], [3,2,1]

Clarifying Questions

What if nums is empty?
A: Nums will have at least one element

Test Cases

[1,2,3] =i/p
[[1,2,3],[2,1,3],[3,2,1],[1,3,2],[2,3,1],[3,1,2]] = o/p

I/p = [1]
O/p = [[1]]

Approach

[__      __      __]
3 ways  2ways   1way

3x2x1 = 6 permutations
3!
                                                        0  1  2
i      j                                swap 0,0        [1,2,3]         swap 0,2
0    0,1,2                       swap 1,1     [1,2,3]   [2,1,3]     [3,2,1]
1     1,2                   [1,2,3]      [1,3,2]    [2,1,3]    [2,3,1]      [3,2,1] [3,1,2]     
2       2   BASE CASE


'''

def permute(nums):
    n = len(nums)
    res = []
    def helper(index):
        #base case
        if index == n-1: 
            res.append(nums[:])
            return
        for j in range(index, n):
            nums[index],nums[j] = nums[j],nums[index]
            helper(index+1)
            nums[index],nums[j] = nums[j],nums[index] #Backtracking step

    helper(0)
    return res

print(permute([1,2,3]))