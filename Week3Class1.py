from collections import deque 


#Problem 1: Post Format Validator
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
a string with openinng and closing () {} []
O - Outputs
a boolean leting us know if the opening mathces with a closing 
C - Constraints
Every opening tag has a corresponding closing tag of the same type.

E - Edge Cases (and examples)

--- PLAN ---
use a stack
--- IMPLEMENT ---

'''
def is_valid_post_format(posts):
  # 1. Initialize our stack
    stack = []
    
    # 2. Dictionary mapping closing tags to opening tags
    matching_tags = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # 3. Loop through the post string
    for char in posts:
        # 4. If it's a closing tag
        if char in matching_tags:
            # 4a & 4b. Pop the top tag (or use a dummy value if stack is empty)
            top_element = stack.pop() if stack else '#'
            
            # 4c. Compare the popped tag to the correct opening tag
            if matching_tags[char] != top_element:
                return False
                
        # 5. If it's an opening tag, push it to the stack
        else:
            stack.append(char)
            
    # 6. If stack is empty, everything matched perfectly!
    return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

#Problem 2: Reverse User Comments Queue
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
array of strings
O - Outputs
another array of strings with the reverse order sorrt
C - Constraints
use a stack
E - Edge Cases (and examples)

--- PLAN ---

--- IMPLEMENT ---

'''
def reverse_comments_queue(comments):
    return_list = []
    """ for i in range(len(comments)-1 , -1, -1):
        return_list.append(comments[i]) """
    while len(comments) > 0:
        return_list.append(comments.pop())
    return return_list 

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


#Problem 3: Check Symmetry in Post Titles
def is_symmetrical_title(title):
    new_str = ""
    for char in title:
        if char.isalnum():
            new_str += char.lower()
    i = 0
    j = len(new_str) - 1

    while i < len(new_str) / 2:
        if new_str[i] != new_str[j]:
            return False
        i += 1
        j -= 1  
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))

#Problem 4: Engagement Boost
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result
    
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

#Problem 5: Content Cleaner
''' UMPIRE TEMPLATE

--- UNDERSTAND ---
I - Inputs: A string `post` containing lowercase and uppercase letters.
O - Outputs: A "clean" string where no adjacent characters are the same letter with different cases.
C - Constraints: The removal cascades. If removing a pair creates a new pair, that new pair must also be removed.
E - Edge Cases:
    - An empty string (returns an empty string).
    - A string with a single character (returns the single character).
    - A string where everything cancels out, like "abBAcC" (returns an empty string).

--- MATCH ---
This is a variation of the "Valid Parentheses" problem we solved earlier! We will use a **Stack**. 
As we read through the post, we will look at the top item on our stack. If the current letter is the exact same letter as the top item, but the opposite case, they destroy each other (we pop it off the stack). Otherwise, we push the letter onto the stack.

To check for opposite cases easily in Python, we can use the built-in `.swapcase()` string method! If `char.swapcase() == top_of_stack`, they are a match to be destroyed.

--- PLAN ---
1. Create an empty list called `stack`.
2. Loop through each character `char` in the input `post`.
3. Check if the stack has items inside it.
4. If it does, check if the current `char` is the opposite case of the very last item in the stack (`stack[-1]`).
5. If they are opposites, pop the top item off the stack (they cancel out!).
6. If they are NOT opposites (or if the stack is empty), append the current `char` to the stack.
7. After the loop finishes, stitch the characters in the stack back together into a single string using `"".join()` and return it.

--- IMPLEMENT ---
'''
def clean_post(post):
    stack = []
    # Step 2: Loop through the post
    for char in post:
        
        # Step 3 & 4: Check if stack isn't empty AND the cases are exact opposites
        if len(stack) > 0 and char.swapcase() == stack[-1]:
            # Step 5: They cancel out! Pop the top character and do nothing else.
            stack.pop()
            
        else:
            # Step 6: No match, so push it onto the stack
            stack.append(char)
            
    # Step 7: Join the surviving characters back into a string
    return "".join(stack)
        


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 


#Problem 6: Post Editor

def edit_post(post):
    queue = deque()
    newPost = ""
    """ using reverse string
    for word in post.split():
        newWord = word[::-1] + " "
        newPost += newWord
        return newPost
        """

    # using queues
    # Step 2: Split into words
    words = post.split()
    reversed_words = []
    
    # Step 4: Process each word
    for word in words:
        # Step 5: Initialize a fresh queue for this specific word
        queue = deque()
        
        # Step 6: Push characters to the FRONT of the queue
        for char in word:
            queue.appendleft(char)
            
        new_word = ""
        
        # Step 7 & 8: Empty the queue from the front
        while len(queue) > 0:
            new_word += queue.popleft()
            
        # Step 9: Save the fully reversed word
        reversed_words.append(new_word)
        
    # Step 10: Stitch the sentence back together
    return " ".join(reversed_words)


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 


#Problem 7: Post Compare
# firt fuction to compare, helper function to delete the backspace chars
def post_compare(draft1, draft2):
    return help_compare(draft1)  == help_compare(draft2)

def help_compare(word):
    new_word = list(word)
    result = []

    for i in range(0,len(word)):
        if word[i] == "#":
            if len(result) > 0:
                result.pop()
        else:
            result.append(new_word[i])
    return result

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 

#set version 2

#Problem 1: Time Needed to Stream Movies
def time_required_to_stream(movies, k):
  pass


print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 