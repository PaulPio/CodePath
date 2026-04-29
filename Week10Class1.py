from collections import Counter
#Problem 1: Graphing Flights
"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here
flights = {
    "LAX" : "JFK",
    "JFK": ["DFW" , "LAX"],
    "DFW": ["JFK", "ATL"],
    "ATL" : "DFW"
}

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

#Problem 2: There and Back
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
            return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

#Problem 3: Finding Direct Flights
def get_direct_flights(flights, source):
    result = []
    for i in range(len(flights[source])):
        if flights[source][i] == 1:
            result.append(i)
    return result


flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))


#Problem 4: Converting Flight Representations
def get_adj_dict(flights):
    d = {}
    for ls in flights:
        if ls[0] in d:
            d[ls[0]].append(ls[1])
        else:
            d[ls[0]] = [ls[1]]

        if ls[1] in d:
            d[ls[1]].append(ls[0])
        else:
            d[ls[1]] = [ls[0]]
    return d
        


flights = [['Cape Town', 'Addis Ababa'], 
            ['Cairo', 'Lagos'],
            ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], 
            ['Cairo', 'Cape Town']
            ]
print(get_adj_dict(flights))
#Problem 5: Find Center of Airport
def find_center(terminals):
    result = []
    for i in range(len(terminals)):
        for j in terminals[i]:
            result.append(j)
    return Counter(result).most_common(1)[0][0]

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

#Problem 6: Finding All Reachable Destinations
def get_all_destinations(flights, start):
    pass

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))