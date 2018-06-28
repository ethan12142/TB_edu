import json
from collections import defaultdict
import ast

with open('parents.json', 'r') as f:
    parents = json.load(f)
pars = ast.literal_eval(parents)
with open('activities.json', 'r') as f:
    acts = json.load(f)
acts = ast.literal_eval(acts)
for i in range(len(acts)):
    print acts[i]['age'][0]
# print acts[0]['age'][0]
# print len(pars['Henry']['age'])
# print type(int(pars['Henry']['act'][0]))
print len(acts[0]['activity'])
check = 0
flag = 1
while check != flag:
    flag = check
    for mom in pars.keys():
        # print mom
        if pars[mom]['age'][0] != '':
            for ages in range(len(pars[mom]['age'])):
                tmp_age = pars[mom]['age'][ages]
                for i in range(len(acts)):
                    if pars[mom]['act'][ages] == '-1':
                        break
                    if acts[i]['age'][0] == tmp_age:
                        num = pars[mom]['act'][ages]
                        if int(num) != len(acts[i]['activity']):
                            check += 1
                            print "Dear", mom, ": The activity for your child,",pars[mom]['childName'][ages],", is \" ",acts[i]['activity'][int(num)],"\"", num
                            pars[mom]['act'][ages] = int(pars[mom]['act'][ages]) + 1
                            if int(pars[mom]['act'][ages]) == len(acts[i]['activity']):
                                print "Curriculum complete!"
                                pars[mom]['act'][ages] = '-1'
                            break
print pars
