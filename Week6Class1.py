"""
UMPIRE template 

  # Understand 
	inputs:
	outputs:
	constraints:
	edge cases:

  # Match

  # Plan
  
  # Implement

  # Review

  # Evaluate
"""
"""
Problem 1: Building a Playlist
The assignment statement to the top_hits_2010s variable below creates the linked list
Uptown Funk -> Party Rock Anthem -> Bad Romance.
Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.
"""

# class SongNode:
#     def __init__(self, song, next=None):
#         self.song = song
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
        
# # top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# node3 = SongNode('Bad Romance')
# node2 = SongNode('Party Rock Anthem',node3)
# node1 = SongNode('Uptown Funk',node2)
# print_linked_list(node1)

# # Uptown Funk -> Party Rock Anthem -> Bad Romance

"""
Problem 2: Top Artists

Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.
Evaluate the time complexity of your solution.
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

UMPIRE template 

  # Understand 
	inputs: head of linked list  
	outputs: dictionary with artist and frequency 
	constraints: explain time complexity 
	edge cases: only one node, upper and lower is the same

  # Match

  # Plan
  1. go through the linked list while there is a head while loop
  2. use a dictionary to count the frequency of a artist
  
  # Implement

  # Review
  
  # Evaluate
  space: O(n)
  time: O(n)
"""

# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# def get_artist_frequency(playlist):
#     current = playlist
#     dic = {}
#     while current:
#       if current.artist in dic:
#         dic[current.artist] += 1
#       else: 
#         dic[current.artist] = 1
#       current = current.next
        
#     return dic
    

# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))
# # { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}

# playlist = SongNode("Saturn", "SZA")
# print(get_artist_frequency(playlist))

"""
Problem 3: Glitching Out

The following code attempts to remove the first node with a given song
from a singly linked list with head playlist_head but it contains a bug!

Step 1: Copy this code into your IDE.
Step 2: Create your own test cases to run the code against,
		and use print statements and the stack trace to identify and fix the bug
        so that the function correctly removes a node by value from the list.
Step 3: Evaluate the time and space complexity of the fixed solution.
		Define your variables and provide a rationale for why you believe
        the solution has the stated time and space complexity.
"""

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
        
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head: # edge case
        return None
    if playlist_head.song == song: # edge case
        print("list head is the song to remove")
        return playlist_head.next
    if playlist_head.song is None:
        print("There is song to remove")
        return playlist_head
    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next
    print("song not found")
    return playlist_head


playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

new_playlist = SongNode("Bohemian Rapsody", "Queen")
new2_playlist = SongNode(None, "Queen")




print_linked_list(remove_song(playlist, "Dreams"))
print_linked_list(remove_song(new_playlist, "Bohemian Rapsody"))
print_linked_list(remove_song(new2_playlist, "Bohemian Rapsody"))
print_linked_list(remove_song(playlist, "Bohemian Rapsody"))


"""
Problem 4: On Repeat

A variation of the two-pointer technique introduced in previous units
is to have a slow and a fast pointer that increment at different rates.

We would like to check whether our playlist loops or not.
Given the head of a linked list playlist_head, return True if the playlist has a cycle in it and False otherwise.
A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution.
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
UMPIRE template 

  # Understand 
	inputs: playlist_head -> head of the linked list
	outputs: boolean -> if the playlist has a cycle
	constraints:
	edge cases:
    	if playlist_head is none or the only node in the linked list

  # Match
	slow and fast pointer
  # Plan
	define a slow and a fast pointer
    slow pointer moves one node at a time
    fast pointer moves two nodes at time
    if they meet then there's a cycle
    otherwise if the fast pointer reaches the end (if its None) then theres no cycle	
  
  # Implement

  # Review

  # Evaluate
"""

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
	slow = playlist_head
	fast = playlist_head
    
	# O -> O -> O -> O -> None
	# 					   f 
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
            
		if slow == fast:
			return True
          
	return False
        

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = None

print(on_repeat(song1))
# True