from collections import Counter
#Linked Lists
#Problem 1: New Horizons
class Villager:
    def __init__(self, name, species, catchphrase ,personality = "Outgoing", neighbor=None):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        self.personality = personality
        self.neighbor = neighbor

    def set_catchphrase(self, new_catchphrase):
        self.catchphrase = new_catchphrase

    def add_item(self, item_name):
        inventory = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in inventory:
            self.furniture.append(item_name)
        else:
            print("Item not in inventory")

    def print_inventory(self):
        # Implement the method here
        inventory_count = Counter(self.furniture)
        inventory = []
        if not self.furniture:
            return print("Inventory empty")

        for key, value in inventory_count.items():
            count = f"{key}: {value}"
            inventory.append(count)  #acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2

        #print(f"{things.items()}")
        return print(", ".join(inventory))

    def of_personality_type(townies, personality_type):
        stack = []
        for person in townies:
            if person.personality == personality_type:
                stack.append(person.name) #adding person name
        return stack
    """
    current = start_villager
    while current is true
        if current ==  target_villager
            return True
        else
            current = current.neighbor
    return False
    """
    def message_received(start_villager, target_villager):
        current = start_villager
        while current:
            if current == target_villager:
                return True
            else:
                current = current.neighbor
        return False


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

#Problem 2: Greet Player
def greet_player(self, player_name):
    return print (f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!")

bones = Villager("Bones", "Dog", "yip yip")
greet_player(bones, "Paul")

#Problem 3: Update Catchphrase

bones.catchphrase = "ruff it up"

greet_player(bones, "Samia")

#Problem 4: Set Character
bones.set_catchphrase("vasasdasdasdas")
greet_player(bones, "Samia")
alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

#Problem 5: Add Furniture

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

#Problem 6: Print Inventory
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
bones.print_inventory()
#Problem 7: Group by Personality

isabelle = Villager("Isabelle", "Dog", "what's up?" , "Normal")
bob = Villager("Bob", "Cat","pthhhpth", "Lazy")
stitches = Villager("Stitches", "Cub","stuffin", "Lazy")

print(Villager.of_personality_type([isabelle, bob, stitches], "Lazy"))
print(Villager.of_personality_type([isabelle, bob, stitches], "Cranky"))

#Problem 8: Telephone
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(Villager.message_received(isabelle, kk_slider))
print(Villager.message_received(kk_slider, isabelle))

#Problem 9: Nook's Cranny

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
print(tom_nook.value) 
print(tom_nook.next.value) 
print(tommy.value) 
print(tommy.next) 

#Problem 10: Timmy and Tommy
timmy = Node("Timmy") 
tom_nook.next = timmy
timmy.next = tommy 

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)

#Problem 11: Saharah
saharah = Node("Saharah")
tommy.next = saharah 
tom_nook.next = None
print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 

#Problem 12: Print Players Linked List
def print_list(head):
    current = head
    while current:
        if current.next:
            print(f"{current.value} ->", end=" ")
        else:
            # If this is the last node, print just the value
            print(current.value)
        current = current.next
        
        

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj
print_list(isabelle)

#Problem Set Version 2
#Problem 1: Instantiate an Instance of Player
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

player_one = Player("Yoshi", "Super Blooper")

print(player_one.character)
print(player_one.kart)
print(player_one.items)