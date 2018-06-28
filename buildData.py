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

# def del_u(s):
#     """remove the leading unicode designator from a string"""
#     new_s = ''
#     if s.startswith("u'"):
#         new_s = s.replace("u'", "'", 1)
#     elif s.startswith('u"'):
#         new_s = s.replace('u"', '"', 1)
#     return new_s

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
    # print "Input Mom:%s",momName, "Child:%s",childName, "Age:%s",age ," succeessfully!!"
    print "Input Mom:%10s, Child:%10s, Age:%s , succeessfully!!" % (momName,childName,age)
# parents = {}
# monInfo = defaultdict(list)
# monInfo['childName'].append('Calvin')
# monInfo['childName'].append('Bill')
# monInfo['age'].append('3')
# monInfo['age'].append('2')

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

parents = {}
addMomInfo('Henry','Calvin','1')
addMomInfo('Ada', 'Lily', '4')
addMomInfo('Emilia', 'Petra', '2')
addMomInfo('Biff', 'Biff Jr', '3')
addMomInfo('Milo','','')

# addMomInfo('Milo','tttt','6')
# print parents['Milo']['childName'] == ['']
# parents['Milo'] = {}

flag = input("Do you want to input new data to parents?(yes:1 no:0)")
while flag:
    mom = raw_input("Please input Mom's name:")
    child = raw_input("Please input Child's name:")
    age = raw_input("Please input Child's age:")
    addMomInfo(mom, child, age)
    flag = input("Do you want to input new data to parents?(yes:1 no:0)")
json_str = json.dumps(parents)
with open('parents.json', 'w') as f:
    json.dump(json_str, f)
# print parents

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

index = input("Do you want to input new data to activities?(yes:1 no:0)")
while index:
    age = raw_input("Please input activity's age:")
    act = raw_input("Please input the activity for your input age:")
    addActivities(age,act)
    index = input("Do you want to input new data to activities?(yes:1 no:0)")
json_act = json.dumps(activities)
with open('activities.json', 'w') as f:
    json.dump(json_act, f)
# print activities
