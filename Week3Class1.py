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