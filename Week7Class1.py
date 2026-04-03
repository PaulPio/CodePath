#Problem 1: Counting Iron Man's Suits
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    count = 0
    if count_suits_iterative(suits) == 0:
        return count
    else:
        count += 1
        return count + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

#Problem 2: Collecting Infinity Stones
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs - > an int array
O - Outputs -> the sum of all the elements in the array
C - Constraints -> using a recursive method
E - Edge Cases (and examples) 
d - base case -> 

--- PLAN ---
count = 0
list = stones.copy()
if len(stones) == 0:
    return 0
else:
    return sumstones([0]) + sumstonesstones([1:]
--- IMPLEMENT ---

'''
def sum_stones(stones):
    if len(stones) == 0:
        return 0
    else:
        return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

#Problem 3: Counting Iron Man's Unique Suits (duplicateds)
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
O - Outputs
C - Constraints
E - Edge Cases (and examples)

--- PLAN ---

--- IMPLEMENT ---

'''
def count_suits_iterative2(suits):
    count = 0
    for suit in set(suits):
        count += 1
    return count

def count_suits_recursive2(suits):
    count = 0
    finalCountsuits = list(set(suits))
    if count_suits_iterative2(finalCountsuits) == 0:
        return count
    else:
        count += 1
        return count + count_suits_recursive(finalCountsuits[1:])

print(count_suits_iterative2(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive2(["Mark I", "Mark I", "Mark III"]))

#Problem 4: Calculating Groot's Growth
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs -> an int
O - Outputs -> the fiboanncy sequence result, an int
C - Constraints -> we have to do it recursevly
E - Edge Cases (and examples)

--- PLAN ---
if n == 0 or n == 1:
    return n
else
    return fiboonacy(n-1) + fibonnacy (n-2) 
--- IMPLEMENT ---

'''
def fibonacci_growth(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_growth(n-1) + fibonacci_growth(n-2) 

print(fibonacci_growth(5))
print(fibonacci_growth(8))

#Problem 5: Calculating the Power of the Fantastic Four
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs - > an int with the value of the exponenet
O - Outputs -> an int with the result of the operation
C - Constraints -> recursive function
E - Edge Cases (and examples)

--- PLAN ---
base case n == 0
if n == 0
    return 1
else:
    return 4 * power_of_four(n-1)
--- IMPLEMENT ---

'''
def power_of_four(n):
    #return 4 ** n
    if n == 0:
        return 1
    else:
        return 4 * power_of_four(n-1) if n>=0 else (1/4) * (power_of_four(n+1))

print(power_of_four(2))
print(power_of_four(-2))

#Problem 6: Strongest Avenger
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs -> an array of ints containing the stats of the avengers strength
O - Outputs ->the result of comparing all elements in the list, and returning the highest value one 
C - Constraints -> recursively
E - Edge Cases (and examples)

--- PLAN ---
maximum = strenght[0] # will get update it with the first one and that one will be the maximum
base case len stregnht = 0
    if len(strenght) == 0:
        return maximum
    else:
        return strongest_avenger(strengths[1:]) if strenght[0] > strenght[1] else strongest_avenger[0]
--- IMPLEMENT ---

'''

def strongest_avenger(strengths):
    # 1. Base case: if there's only 1 item, return it
    if len(strengths) == 1:
        return strengths[0]
    # 2. Get the maximum of the rest of the list
    max_of_rest = strongest_avenger(strengths[1:])
    
    # 3. Return the larger of the two
    if strengths[0] > max_of_rest:
        return strengths[0]
    else:
        return max_of_rest

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))