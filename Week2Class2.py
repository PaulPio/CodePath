#Problem 1: Festival Lineup
def lineup(artists, set_times):
    pass

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


#Problem 1: Space Crew
def space_crew(crew, position):
    roles = {}
    for i in range(len(crew)):
        roles[crew[i]] = position[i]
    return roles
exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))


#Problem 2: Space Encyclopedia
def planet_lookup(planet_name):
    if planetary_info.get(planet_name) == None:
        return "Sorry, I have no data on that planet."
    else:
        return "Planet " + str(planet_name) + " has an orbital period of " + str(planetary_info.get(planet_name).get("Orbital Period")) + " Earth days and has " + str(planetary_info.get(planet_name).get("Moons")) + " moons."

planetary_info = {
    "Mercury": {        
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))


#Problem 3: Breathing Room

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    outside = []
    for i in oxygen_levels:
        if oxygen_levels[i] < min_val or oxygen_levels[i] > max_val:
            outside.append(i)
    return outside

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))


#Problem 4: Experiment Analysis
def data_difference(experiment1, experiment2):
    # 1. Initialize an empty dictionary to store the differences
    diff_dict = {}

    # 2. Loop through each key-value pair in the first experiment
    for key, value in experiment1.items():
        
        # 3. Check if the key exists in experiment2 AND has the same value
        # We only want to keep the data if the exact pair is NOT in experiment2
        if key not in experiment2 or experiment2[key] != value:
            
            # 4. Add the unique key-value pair to our new dictionary
            diff_dict[key] = value

    # 5. Return the final result
    return diff_dict

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))