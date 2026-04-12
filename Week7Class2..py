import bisect
#def find_cruise_length(cruise_lengths, vacation_length):
def find_cruise_length(cruise_lengths, vacation_length):
    ''' UPI TEMPLATE

    --- UNDERSTAND ---

    I - Inputs
    O - Outputs
    C - Constraints
    E - Edge Cases (and examples)

    --- PLAN ---

    --- IMPLEMENT ---

    '''
    low = 0
    high = len(cruise_lengths) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if cruise_lengths[mid] < vacation_length:
            low = mid + 1
        elif cruise_lengths[mid] > vacation_length:
            high = mid - 1
        else:
            return True
            
    
    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


#Problem 2: Booking the Perfect Cruise Cabin
def find_cabin_index(cabins, preferred_deck, low=0, high=None):
    if high is None:
        high = len(cabins) - 1
        
    # Base case: if low is greater than high, the element is not found.
    # The `low` pointer will actually be exactly at the correct insertion index!
    if low > high:
        return low
        
    mid = low + (high - low) // 2
    
    # If the preferred deck is found
    if cabins[mid] == preferred_deck:
        return mid
        
    # If the value at mid is less than preferred, search the right half
    elif cabins[mid] < preferred_deck:
        return find_cabin_index(cabins, preferred_deck, mid + 1, high)
        
    # If the value at mid is greater than preferred, search the left half
    else:
        return find_cabin_index(cabins, preferred_deck, low, mid - 1)
    


print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))

#Problem 3: Count Checked In Passengers
def count_checked_in_passengers(rooms):
    ''' UPI TEMPLATE

        --- UNDERSTAND ---

        I - Inputs
        an array with ints that represent the status of the reservations
        O - Outputs
        a count of the number of checkin reservations
        C - Constraints
        has to be log n
        E - Edge Cases (and examples)
        array is empty, non int on the array, any other data type
        --- PLAN ---
        
        find the first index of 1, return index - len(rooms) if target is found else return 0
        --- IMPLEMENT ---
        return rooms.count(1)

        '''
    n = len(rooms)
    left, right = 0, n - 1
    first_one_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if rooms[mid] == 1:
            # We found a 1, but is it the FIRST one?
            first_one_index = mid
            # Keep looking on the left side to be sure
            right = mid - 1
        else:
            # It's a 0, so the 1s must be to the right
            left = mid + 1
            
    # If first_one_index is still -1, there were no 1s
    if first_one_index == -1:
        return 0
    
    # Calculate count based on position
    return n - first_one_index


rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))

#Problem 4: Determining Profitability of Excursions
def is_profitable(excursion_counts):
    return excursion_counts[1] - excursion_counts[0] if excursion_counts[0] > 0 else -1


print(is_profitable([3, 5]))
print(is_profitable([0, 0]))

#Problem 5: Finding the Shallowest Point
def find_shallowest_point(depths):
    pass

print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))