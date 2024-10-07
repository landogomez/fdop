'''
Josephus Problems

There are n friends that are playing a game. The friends are sitting in a circle and are numbered
from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the
(i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend bringd you to the 1st friend.
The rules of the game are as follows:
1. Start at the 1st friend.
2. Count the next k friends in the clockwise direction including the friend you started at. The counting
wraps around the circle and may count some friends more than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, go back to step 2 starting from the friend 
inmmediately clockwise of the friend who just lost and repeat.
5. Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.


Eg. n=4, k=2 
    1
 4      2
    3    
we start at 1 and count 1,2 so 2 losses and we got

    1
4       3
We start now counting at 3, 1 = 3, 2=4 so for losses
    1
    3
We start on 1 now, so 1 = 1, 2 = 3, 3 losses and only 1 is left so he one the game
we return the winner, in this case is 1

Test Cases
n=1
k=3 
o/p = 1

n=2
k=3
o/p = 1

Aproach 1 

Observations

-> Notice the problem is defined Recursively
-> When you have something circular, consider % (modulo)

Lets see if we can just use an array
k = 7
n = 5

[1,2,3,4,5]
 0 1 2 3 4 

7%5 = 2
start at 0
[0+7-1] % 5 // Se resta uno porque el arreglo comienza en 0
[6]%5 = index 1
index = 2, so 2 is the first person that has to leave the game
and all of this is the recursive case

Base Case
if len(array) = 1 : return arr[0]

Pseudocode

Function Winner(arr, start)
if len(array) = 1: return arr[0]
else: remove = [start + k-1]%len
delete -> arr[remove] remove = index we just delete
Winner(arr, remove) 

eg [1,2,3,4,5]
    0 1 2 3 4       2 has to leave, so now we hav

    [1,3,4,5]
     0 1 2 3        The game says we need to start to the left of the guy that just leaved in this case
                    3 and is the same index that 2 was before

Time and Spcae complexity
we call the function n time O(n)

In each call we remove one element which is O(n)

T = O(n)**2
S = O(n)
'''

def findTheWinner(n, k):
    # creating n=4, arr=[1,2,3,4]
    arr = [i+1 for i in range(n)]

    def helper(arr, start_index):
        #base case
        if len(arr) == 1:
            return arr[0]
        
        #recursive case
        index_to_remove = (start_index + k -1) % len(arr)
        del arr[index_to_remove]
        return helper(arr, index_to_remove)
    
    return helper(arr,0)
print(findTheWinner(5,7))

