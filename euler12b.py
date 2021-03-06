# already tested n < 16 000 000 with no result.

'''
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding 
the natural numbers. So the 7th triangle number would 
be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms 
would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over 
five divisors.

What is the value of the first triangle number to have over 
five hundred divisors?
'''
# Triangular numbers are sums of consective whole numbers in range (1, n).

# ie. 1st triangular number = 1
# 2nd triangular number = 1 + 2 = 3
# 3rd triangular number = 1 + 2 + 3 = 6
# etc.

import timeit
start = timeit.default_timer()

n = 1
tri_num = 0
max_factors = 0
tri_num_w_mostfactors = 0

while max_factors <= 500:
    tri_num = tri_num + n   
    print(tri_num)    
    
    # This part is for counting factors of each tri_num
    count_factors = 0
    
    for d in range(1, tri_num+1):
        if tri_num%d==0:
            print(str(d) + " is a factor of " + str(tri_num))
            count_factors += 1            
        else:
            continue    
    
    print("The number " + str(tri_num) + " has " + str(count_factors) + " factors.")
    if count_factors > max_factors:
        max_factors = count_factors
        tri_num_w_mostfactors = tri_num 
    
    n += 1

print("The number with most factors is: " + str(tri_num_w_mostfactors) + ". It has " + str(max_factors) + " many factors.")


stop = timeit.default_timer()
first_attempt = (stop - start)
print(first_attempt)




