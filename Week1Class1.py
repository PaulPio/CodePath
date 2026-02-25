"""
First class of CodePath
"""

#Problem 1: Hundred Acre Wood
def welcome():
    print("Welcome to the Hundred Acred Wood")

welcome()



#Problem 2: Greeting
def greeting(name):
    print(f"Hello {name}")

greeting("Pooh")

#Problem 3: Catchphrase
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh brother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
        
print_catchphrase("samuel")

#problema 4: : Return Item
def get_items(items, x):
    if x <= len(items):
        return items[x]
    else:
        return None

print(get_items(["apple", "banana", "cherry"], 1))

#Problem 5: Total Honey
def sum_honey(hunny_jars):
    count = 0
    for i in hunny_jars:
        count = count + i
    print(count)
    
hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)
hunny_jars = []
sum_honey(hunny_jars)

#Problem 6: Double Trouble
def double_trouble(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    print(hunny_jars)
    
hunny_jars = [2, 3, 4, 5]
double_trouble(hunny_jars)

#Problem 7: Poohsticks
def count_less_than(race_times, threshold):
    count = 0
    for i in race_times:
        if i < threshold:
            count += 1
    print(count)

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)

#Problem 8: Pooh's To Do's
def print_todo_list(task):
    print("Pooh's To Dos:")
    for i in range (len(task)):
        print(f"{i+1}. {task[i]}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

#Problem 9: Pairs
def can_pair(item_quantities):
    for i in range(len(item_quantities)):
        if (item_quantities[i] % 2 != 0):
            print("False")
            return
    print("True")

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
 
 #Problem 10: Split Haycorns
def split_haycorns(quantity):
    list = []
    for i in range (1 , quantity +1):
        if quantity  % i == 0:
            list.append(i)
    print(list)

    

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)