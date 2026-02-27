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
    O - Outputs 
    C - Constraints 
    E - Edge Cases (and examples)

--- PLAN --- 

--- IMPLEMENT --- 

'''

def final_value_after_operations(operations):
	pass

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)