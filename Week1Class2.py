#Problem 1: Reverse Sentence
def reverse_sentence(sentence):
    #use the split method to divide the string
    sentence = sentence.split()
    sentence = sentence[::-1]
    new_sentence = ""
    for word in sentence:
        new_sentence = new_sentence + " " +  word
    new_sentence = new_sentence[1:]
    print (new_sentence)

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)


#Problem 2: Goldilocks Number

def goldilocks_approved(nums):
    nums.remove(min(nums))
    nums.remove(max(nums))

    if len(nums) > 0:
        print(nums[0])
    else:
        print(-1)
        return -1



nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)


#Problem 3: Delete Minimum
''' UPI TEMPLATE 

--- UNDERSTAND ---

    I - Inputs 
    int array
    O - Outputs
    int array but arranged in the order of remove items 
    C - Constraints 
    we have to return in the order of remove items 
    E - Edge Cases (and examples)
    empty array , if statement
    duplicated elemnts, 

--- PLAN --- 

make a new empty array

if validation if the array is empty

develop a for loop to add  the elemnet to the new array  and after that remove the min element

print result

--- IMPLEMENT --- 

'''
def delete_minimum_elements(hunny_jar_sizes):
    jars = []
    if(len(hunny_jar_sizes) > 0):
        for i in range(len(hunny_jar_sizes)):
            jars.append(min(hunny_jar_sizes))
            hunny_jar_sizes.remove(min(hunny_jar_sizes))
    else:
        return None
    print(jars)
    
hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)

#Problem 4: Sum of Digits
''' UPI TEMPLATE 

--- UNDERSTAND ---

    I - Inputs 
    int
    O - Outputs 
    sum of the digits in the int
    C - Constraints 

    E - Edge Cases (and examples)
    only one digit

--- PLAN --- 

for a loop to separate and then sum the ints

--- IMPLEMENT --- 

'''

def sum_of_digits(num):
    count = 0
    nums = list(str(num))
    for i in nums:
        number = int(i)
        count += number
    print(count)

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)


#Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
''' UPI TEMPLATE 

--- UNDERSTAND ---

    I - Inputs
    list os strings
    O - Outputs 
    counter int variable that reperesents teh final value of tigger
    C - Constraints 
    E - Edge Cases (and examples)
     string that were not accounted for on initial code, any other data type

--- PLAN --- 

a for loop that reads through the array and increase or decresases the count variable depenidng on the content of the string i
--- IMPLEMENT --- 

'''
def final_value_after_operations(operations):
    count = 1
    for word in operations:
        if word is "bouncy" or word is "flouncy":
            count += 1
        elif word is "trouncy" or word is "pouncy":
            count -= 1
    print(count)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)


#Problem 6: Acronym
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
array of strings and a string
O - Outputs
True or False
C - Constraints
E - Edge Cases (and examples)
any data type that is not string, or any array that is not strings
--- PLAN ---

run a for loop through the array to get the first letter of each item in the string array and save them i a new string variable
then compare if the items of the new string variable, mathes with the string s

--- IMPLEMENT ---

'''

def is_acronym(words, s):
    w = ""
    for word in words:
        w += word[0]
    if w == s:
        print ("True")
        return True
    else:
        print ("False")
        return False

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)

#Problem 7: Good Things Come in Threes
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
int array
O - Outputs
an int with the minimun number of operations to make all elements of nums divisible by 3
C - Constraints
E - Edge Cases (and examples)
non int arrays
--- PLAN ---
run a for loop to go thurhg the array, use and if statement checkign the remainder of a division between index i value and 3 equals 0, if not , increase the value of the i value until the remainders is 0, and 
store the number of iterations required to achieve the result in a count variable, 
every time the operation is made through the loop, make an if statement that checks if the current count is higher than the previous count of previous iteration, if higher change value, if less, no

--- IMPLEMENT ---

'''
def make_divisible_by_3(nums):
    count = 0
    for i in nums:
        if i % 3 != 0:
            count += 1
    print(count)

nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)

#Problem 8: Exclusive Elements
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
O - Outputs
C - Constraints
E - Edge Cases (and examples)

--- PLAN ---

--- IMPLEMENT ---

'''
def exclusive_elemts(lst1, lst2):
	pass

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)