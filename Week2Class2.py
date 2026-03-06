#Problem 1: Most Endangered Species
''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
An arra of dictionaries
O - Outputs
String, value of the lowest population dict
C - Constraints
empty array, any other data type that is not dictionary
E - Edge Cases (and examples)

--- PLAN ---
For loop that goes through the array, key, value, 
create a counter called minimum = -100

--- IMPLEMENT ---

'''
def most_endangered(species_list):
    minimum = float("inf")
    endangered_species_name = ""
    for specie in species_list:
        if specie['population'] <= minimum:
            minimum = specie['population']
            endangered_species_name = specie['name']
    return endangered_species_name 


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))


#Problem 2: Identifying Endangered Species

''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
a string 
O - Outputs
the number of endangered species
C - Constraints

E - Edge Cases (and examples)
empty string, any other data type that is not a string, or an array

--- PLAN ---
we have to create one  set to store endangered_species
one int variable to counter the aparitions of endangered_species
a for loop that checks if an item in the set endangered_species is on the string of observed_species,
if it is add one to the counter 
return the counter
--- IMPLEMENT ---

'''

def count_endangered_species(endangered_species, observed_species):
    endangered_species_set = set(endangered_species)
    counter = 0
    endangered_species_set.intersection
    for species in observed_species:
        if species in endangered_species_set: #in is to check if the item is on the set
            counter +=1
    return counter


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

#Problem 3: Navigating the Research Station

''' UPI TEMPLATE

--- UNDERSTAND ---

I - Inputs
2 strings, one with the layout of chars , and another one with the chars to look for
O - Outputs
is a number of times that the for loop moves to get the index of the string
C - Constraints
do the observations in one movement
E - Edge Cases (and examples)
The index moves from 0 to 2 to observe 'c', then to 1 for
'b', then to 0 again for 'a'.

empty string, any other data type that is no string

--- PLAN ---
create a count variable to sum the indexes of the obsetations
create a dictionary using a for loop to store the chars and their posiiton in the layout
key = char
value = index value

for loop using enumerate, 2 values to search for in the for loop , i and j
sum the counter of indexes every
return counter
--- IMPLEMENT ---

'''
def navigate_research_station(station_layout, observations):
    positions = { char : idx for idx, char in enumerate(station_layout)}
    total_time = 0
    current_position = 0
    #target_position = 0
    #print(positions)
    for observation in observations:
        target_position = positions[observation]
        total_time += abs(current_position - target_position )
        current_position = target_position


    return total_time



station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

#Problem 4: Prioritizing Endangered Species Observations

def prioritize_observations(observed_species, priority_species):
  pass


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 
