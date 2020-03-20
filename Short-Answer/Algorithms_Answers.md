#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

a = 0                   O(1)
while (a < n * n * n):  loop size is n^3
    a = a + n * n       a = O(1) + O(n) * O(n)

n = 1
while a < 1: 
    a = a + 1 #loops 1 time

n = 2
while a < 16 (2 * 2 * 2) :
    a = a + 4 (2 * 2) (loops 2 times)

n = 3
while a < 27: 
    a = a + 9 ( loops 3 times)

so because the loop length is n^3 but we're approaching the length at n^2
n^3 / n^2 = O(n)

answer: O(n) 

b)
sum = 0
for i in range(n):  O(n)
    j = 1           O(1)
    while j < n:    O(log(n))
    j *= 2          O(1)
    sum += 1        O(1)

n is our range in the loop. Because j approaches n at double the rate each loop it is a logn relationship. Since taht is nested inside the O(n) outer loop we multiply them together. 

answer: O(nlogn)

c)
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)

recursion can be thought of a different kind of loop. Since we are only calling the function once within itselt the recursion alone is O(n). Evaluating the rest of the expression we can see that if bunnies = 1, bunnyEars == 2 since we hit our base case on the first recursion. 

if bunnies = 2, our recursion runs twice and if 3 it runs 3 times. 
Because we aren't modifying the value of bunnies we can ignore the adding 2 in the return. 

That makes this O(n)

answer: O(n)

## Exercise II
This can be solved with simple recursion. Because we have infinite eggs we don't need to worry about minimizing the number of tests. Our only concern is the number of eggs broken. 

n = building height
f = floor when breaks

Since we know for certain an egg won't be broken if dropped from a floor below f we can test beginning at n = 1 and recursively checking if the egg is broken when dropped

pseudocode: 

def egg_test(n=1): 
    #base case
    if n == f:
        # if the egg breaks, return the floor it broke from
        return n

    #test each floor starting at one until the egg breaks
    egg_test(n+1) 

This will ensure that the maximum eggs broken is 1. Because this loop only runs itself once for each iteration, this would be O(f) where f is the number of iterations. This can also be written as O(n)