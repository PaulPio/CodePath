#Problem 1: Wild Goose Chase
"""UMPIRE: Understand, Match, Plan, Implement, Review, Evaluate.

We’ll apply these six steps to the problems we’ll see in the first half of the course.

We will learn to:

Understand the problem
Match identifies common approaches you've seen/used before
Plan a solution step-by-step, and
Implement the solution
Review your solution
Evaluate your solution's time and space complexity and think critically about the advantages and disadvantages of your chosen approach.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    current = clues
    while current:
        if current.next == clues:
            return True
        current = current.next
    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1
clue4 = Node("The stolen goods are at an abandoned warehouse")


print(is_circular(clue1))
print(is_circular(clue4))

#Problem 2: Breaking the Cycle
"""UMPIRE: Understand, Match, Plan, Implement, Review, Evaluate.

We’ll apply these six steps to the problems we’ll see in the first half of the course.

We will learn to:

Understand the problem ->
Match identifies common approaches you've seen/used before
Plan a solution step-by-step, and
Implement the solution
Review your solution
Evaluate your solution's time and space complexity and think critically about the advantages and disadvantages of your chosen approach.
"""
def collect_false_evidence(evidence):
    cycle = set()
    result_values= []
    current = evidence
    start = None
    
    while current:
        if current in cycle:
            start = current
            break
        cycle.add(current)
        current = current.next

    if not start:
        return [] 
    #add value to begin results
    result_values.append(start.value)
    current = start.next
    
    while current != start:
        result_values.append(current.value)
        current = current.next

    return result_values
    



clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

#Problem 3: Prioritizing Suspects
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    temp_head = Node(1) # Initialize a temporary head node
    temp_head.next = suspect_ratings    # Point the temporary head at the input list


suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))