# The scores dataset is a list of dictionaries one of whose entries is given below for your reference:
# {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}
# Write the following functions:
# (1) group_by_city: accepts the scores_dataset as argument. It should return a dictionary named cities whose keys are names of the cities that the students are from. The value corresponding to a key (city) is the list of names of all students who hail from this city. The order in which names are appended to the list doesn't matter.
# (2) busy_cities: accepts the scores_dataset as argument. It should return a list of cities. Each city in this list has the property that the number of students from this city is greater than or equal to the number of students from every other city in the dataset. Your function should make use of group_by_city. The order in which the cities appended to the list doesn't matter.
# Input                                                      Expected Output
# Test Case1
# 200
# group_by_city(scores_dataset)                               Dispur:['Hardik', 'Sachin', 'Uma']
#                                                             Srinagar:['Anirban', 'Arshad', 'Fatima']
#                                                             Pune:['Karthik', 'Mary', 'Ram', 'Ria']
#                                                             Shillong:['Gopi', 'Kareena']
#                                                             Bhopal:['Jasmine', 'Naveen']
# Test Case2
# 1100
# busy_cities(scores_dataset)                                 ['Bengaluru', 'Delhi', 'Nagpur']

def group_by_city(scores_dataset):
    cities = dict()

    for student in scores_dataset:
        city = student['City']
        name = student['Name']
        if city not in cities:
            cities[city] = [ ]
        cities[city].append(name)

    return cities

def busy_cities(scores_dataset):
    cities = group_by_city(scores_dataset)

    busy = [ ]
    maxpop = 0
    for city in cities:
        if len(cities[city]) > maxpop:
            maxpop = len(cities[city])
            busy = [city]
        elif len(cities[city]) == maxpop:
            busy.append(city)

    return busy