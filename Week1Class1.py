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

#Problem 11: T-I-Double Guh-ER
def tiggerfy(s):
    # letters Tigger steals (both cases if you want)
    steal = "tigerTIGER"
    
    # build a list of characters to keep
    kept_chars = []
    for ch in s:
        if ch not in steal:
            kept_chars.append(ch)
    
    # join list into a string and return
    return "".join(kept_chars)


s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))


#Problem 12: Thistle Hunt
def locate_thistles(items):
    list = []
    for i in range(len(items)):
        if items[i] == "thistle":
            list.append(i)
    print(list)




items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)

#Problem 1: Batman
def batman():
	print("I am vengeance. I am the night. I am Batman!")

batman()

#Problem 2: Mad Libs
def madlib(verb):
	print(f"I have one power. I never {verb}. - Batman")


verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)

#Problem 3: Trilogy
def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print("Christopher Nolan did not release a Batman movie in 1998.")


year = 2008
trilogy(year)

year = 1998
trilogy(year)

#Problem 4: Last
def get_last(items):
    if (len(items) > 0):
    	print( items[len(items) - 1])
    else:
        return None


items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)

#Problem 5: Concatenate
def concatenate(words):
    letter = ""
    if len(words) > 0:
        for i in words:
            letter += i
    print(letter)    



words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)

#Problem 6: Squared
def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2 
    print(numbers) 
numbers = [1, 2, 3]
squared(numbers)


#Problem 7: NaNaNa Batman!

def nanana_batman(x):
    if x > 0 :
        print(f"{"na" * x} batman!")
    else:
        print("batman!")

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)

#Problem 8: Find the Villain
def find_villain(crowd, villain):
    hiding_places = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            hiding_places.append(i)
    print(hiding_places)
            
crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)


#Problem 9: Odd
def get_odds(nums):
    odds = []
    for num in nums:
        if num % 2 != 0:
            odds.append(num)
    print(odds)


nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)


#Problem 10: Up and Down

def up_and_down(lst):
    count_odd = 0
    count_even = 0
    for num in lst:
        if num % 2 != 0:
            count_odd+=1
        else:
            count_even +=1
    result = count_odd - count_even
    print(result)
    return result



lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)


#Problem 11: Running Sum
def running_sum(superhero_stats):
	pass

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)