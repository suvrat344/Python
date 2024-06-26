# You are given certain details of the trains that stop at a station. Your task is to store these details in a nested dictionary.
# The first line of input is n, the number of trains that stop at the station. n blocks of input follow. The first line in each block corresponds to the train name. The second line in each block corresponds to m, the number of compartments in the train. m lines of input follow. Each of these m lines has two values separated by a comma: name of the compartment and number of passengers in it.
# Your task is to create a nested dictionary named station_dict. The keys of the dictionary are train names, the value corresponding to a key is another dictionary. The keys of the inner dictionary are the compartment names in this train, the values are the number of passengers in each compartment. For example:
# {
#     'Mumbai Express': {
#         'S1': 10,
#         'S2': 20,
#         'S3': 30
#     },
#     'Chennai Express': {
#         'S1': 10,
#         'S2': 20,
#         'S3': 30
#     }
#   }
# (1) The values of the compartments should be represented as integers and not as strings.
# Input                                   Expected Output
# Test Case1
# 2                                       {
# Mumbai Express                            "Chennai Express": {
# 2                                                      "S1": 5,
# S1,10                                                  "S2": 10,
# S2,20                                                  "S3": 15
# Chennai Express                                               },
# 3                                          "Mumbai Express": {
# S1,5                                                   "S1": 10,
# S2,10                                                  "S2": 20
# S3,15                                           }
#                                         }
# Test Case2
# 1                                     {
# Rajdhani Express                                        "Rajdhani Express": {
# 5                                                      "S1": 1,
# S1,1                                                       "S2": 2,
# S2,2                                                       "S3": 10,
# S3,10                                                       "S4": 20,
# S4,20                                                       "S5": 20
# S5,20                                                }
#                                         }

n = int(input("Enter number of train : "))
station_dict = dict()

while n > 0:
    train = input("Enter train name : ")
    num_comps = int(input("Enter number of compartment : "))
    train_dict = dict()
    for i in range(num_comps):
        comp, count = input("Enter name of the compartment and number of passenger separated by comma : ").split(',')
        train_dict[comp] = int(count)
    station_dict[train] = train_dict
    n = n - 1

print(station_dict)