#Problem 1: Mutual Friends
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        selfFriends = self.friends

        set1 = set()
        set2 = set()
        for i in selfFriends:
            set1.add(i.name)
        for i in new_contact.friends:
            set2.add(i.name)
        return list(set1 & set2)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))

#Problem 2: Linked Up
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)

#Problem 3: Daily Tasks
# For testing

def add_first(head, task):
    newNode = Node(task)
    newNode.next = head

    return newNode
     

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))

#Problem 4: Halve List

def halve_list(head):
    current = head
    while current:
        current.value = current.value / 2 
        current = current.next
    return head


node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))


#Problem 5: Remove Last
def delete_tail(head):
    if head is None or head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next
        
    current.next = None
    return head

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))


#Problem 6: Find Minimum in Linked List
def find_min(head):
    current = head
    minimum = float('inf')
    while current:
        if current.value < minimum:
            minimum = current.value
        current = current.next
    return minimum



head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))


#Problem 7: Remove From Inventory
def delete_item(head, item):
    current = head
    while current.next.next is not None:
        if current.next.value == item:
            current.next = current.next.next 
    return head


slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))


#Problem 8: Move Tail to Front of Linked List
def tail_to_head(head):
    current = head
    
    while current.next is not None:
       # print("eee")""" 
        current = current.next
        if current.next.next == None:
            temp = current.next # tail temp value
            current.next = None #new tail
       
    temp.next = head #tail getting assign to head
    return temp


daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad") 
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
print_linked_list(daisy)

print_linked_list(tail_to_head(daisy))


