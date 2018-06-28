'''
Below is the base data requirement.
1. Any mother may has more than one child, so I change the type of mother in parents to list,
   so that we can save as more as children.
2. in order to record which activities mother had used, so I add a list into parents to track
   their schedules.
Base on these two points, my parents structure becomes:

parents = {
    'Henry': {'childName': 'Calvin', 'age': 1, act: 0},
    'Ada': {'childName': 'Lily', 'age': 4, act: 0},
    'Emilia': {'childName': 'Petra', 'age': 2, act: 0},
    'Biff': {'childName': 'Biff Jr', 'age': 3, act: 0},
    'Milo': {'childName': '', 'age': '', act: 0}
}
'''
# parents = {
#     'Henry': {'childName': 'Calvin', 'age': 1},
#     'Ada': {'childName': 'Lily', 'age': 4},
#     'Emilia': {'childName': 'Petra', 'age': 2},
#     'Biff': {'childName': 'Biff Jr', 'age': 3},
#     'Milo': {}
# }
#
# activities = [
#     {
#         'age': 1,
#         'activity': [
#             'Go outside and feel surfaces.',
#             'Try singing a song together.',
#             'Point and name objects.'
#             ]
#     },
#     {
#         'age': 2,
#         'activity': [
#             'Draw with crayons.',
#             'Play with soundmaking toys or instruments.',
#             'Look at family pictures together.'
#             ]
#     },
#     {
#         'age': 3,
#         'activity': [
#             'Build with blocks.',
#             'Try a simple puzzle.',
#             'Read a story together.'
#             ]
#     }
# ]

import json
from collections import defaultdict

#A function which creates Mom's infomation as a dict
def addMomInfo(momName, childName, age):
    monInfo = defaultdict(list)
    monInfo['childName'].append(childName)
    monInfo['age'].append(age)
    monInfo['act'].append('0')
    if momName not in parents.keys():
        parents[momName] = monInfo
    else:
        parents[momName]['childName'].append(childName)
        parents[momName]['age'].append(age)
        parents[momName]['act'].append('0')
    print "Input Mom:%10s, Child:%10s, Age:%s , succeessfully!!" % (momName,childName,age)

#A function which creates Activities infomation as a list
def addActivities(age, act):
    exis = 0
    if len(activities) == 0:
        acts = defaultdict(list)
        acts['age'].append(age)
        acts['activity'].append(act)
        activities.append(acts)
        print "Input age:%2s, activity:%50s , succeessfully!!" % (age,act)
    else:
        for i in range(len(activities)):
            if activities[i]['age'][0] == age:
                activities[i]['activity'].append(act)
                print "Input age:%2s, activity:%50s , succeessfully!!" % (age,act)
                exis = 1
                break
        if exis == 0:
            acts = defaultdict(list)
            acts['age'].append(age)
            acts['activity'].append(act)
            activities.append(acts)
            print "Input age:%2s, activity:%50s , succeessfully!!" % (age,act)

#I manually initialize the base parents data
parents = {}
addMomInfo('Henry','Calvin','1')
addMomInfo('Ada', 'Lily', '4')
addMomInfo('Emilia', 'Petra', '2')
addMomInfo('Biff', 'Biff Jr', '3')
addMomInfo('Milo','','')

#Users can add new data here
flag = input("Do you want to input new data to parents?(yes:1 no:0)")
while flag:
    mom = raw_input("Please input Mom's name:")
    child = raw_input("Please input Child's name:")
    age = raw_input("Please input Child's age:")
    addMomInfo(mom, child, age)
    flag = input("Do you want to input new data to parents?(yes:1 no:0)")
json_str = json.dumps(parents)

#Write down the completed parents data into parents.json
with open('parents.json', 'w') as f:
    json.dump(json_str, f)

#I manually initialize the base activities data
activities = []
addActivities('1','Go outside and feel surfaces.')
addActivities('1','Try singing a song together.')
addActivities('1','Point and name objects.')
addActivities('2','Draw with crayons.')
addActivities('2','Play with soundmaking toys or instruments.')
addActivities('2','Look at family pictures together.')
addActivities('3','Build with blocks.')
addActivities('3','Try a simple puzzle.')
addActivities('3','Read a story together.')

#Users can add new data here
index = input("Do you want to input new data to activities?(yes:1 no:0)")
while index:
    age = raw_input("Please input activity's age:")
    act = raw_input("Please input the activity for your input age:")
    addActivities(age,act)
    index = input("Do you want to input new data to activities?(yes:1 no:0)")
json_act = json.dumps(activities)
#Write down the completed activities data into activities.json
with open('activities.json', 'w') as f:
    json.dump(json_act, f)
