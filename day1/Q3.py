'''
K-TH SYMBOL IN GRAMMAR (RECURSION)

We build a table of n rows (1-idexed). We start by writing 0 in the 1st row. Now in every susequent row, 
we look at the previous row and replace each ocurrence of 0 with 01, and each ocurrence of 1 with 10.
For example, for n=3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows

        0 |n=1
      0   1     n = 2
    0 1  1  0       n = 3
k=1  k=2  k=3 k=4

Clarifying Questions

Is it possible that n is given as 0?
A: No, n >= 1

Can k be out of bound? For eg, If n=3, there will be 4 numbers, can k be given as 5?
A: No, 1<= k <= 2**n-1

Test Cases

n = 4

0           n=1, k=1 -> return 0
01          n=2, k=1 -> return 0
0110        n=4, k=1 -> 0
01101001    n=4, k=8 -> 1
12345678

Methods
n
1    0
2    01
3    0110
4    01101001

Observations: 
1) nth row first half is same as previous row
2) nth row second half is NOT of previous row

base case: n = 1 o/p = 0

T=O(n)
S=O(n)
'''

def kth_symbol(n, k):
    #base case
    if n==1: return 0
    length = 2**(n-1)
    mid = length // 2
    if k <= mid:
        return kth_symbol(n-1, k)
    else:
        return int(not kth_symbol(n-1, k-mid))
        # return 1 - kth_symbol(n-1, k-mid)
print(kth_symbol(4,2))