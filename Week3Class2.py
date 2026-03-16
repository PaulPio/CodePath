# 1. Import the deque module
from collections import deque 
#Problem 1: Manage Performance Stage Changes
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
An array of strings
O - Outputs
An array of chars contaning the perfomances IDs
C - Constraints
E - Edge Cases (and examples)

--- PLAN ---
Create a stack to contain the canceled events
Make a for loop to add to the stack the cancel events and
if cancel is the string on the for loop, pop the element of the shedule 
--- IMPLEMENT ---

'''
def manage_stage_changes(changes):
    cancel_events = []
    scheduled_events = []

    for i in range(len(changes)):
        if changes[i] == "Cancel":
            cancel_events.append(changes[i-1])
            scheduled_events.pop()
        elif changes[i] == "Reschedule":
            scheduled_events.append(cancel_events.pop().replace("Schedule " , ""))
        else:
            scheduled_events.append(changes[i].replace("Schedule " , ""))
    return scheduled_events
            



print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))

#Problem 2: Queue of Performance Requests
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
an array of tuples
O - Outputs
a queue sorted depending on the priority
C - Constraints
E - Edge Cases (and examples)

--- PLAN ---

--- IMPLEMENT ---

'''
def process_performance_requests(requests):
    # Step 2: Sort the list by priority (index 0 of the tuple) in descending order
    # Python's sort is stable, so arrival order for ties is preserved!
    sorted_requests = sorted(requests, key=lambda x: x[0], reverse=True)
    
    # Step 3: Initialize our standard queue
    queue = deque()
    
    # Step 4: Enqueue all the sorted requests
    for request in sorted_requests:
        queue.append(request)
        
    processed_order = []
    
    # Step 6 & 7: Dequeue (popleft) and process them
    while len(queue) > 0:
        current_performance = queue.popleft()
        processed_order.append(current_performance[1])
        
    # Step 8: Return the result
    return processed_order

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))