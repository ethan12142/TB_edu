import json
from collections import defaultdict
import ast

#load parents.json file and save the data into parents
with open('parents.json', 'r') as f:
    parents = json.load(f)
pars = ast.literal_eval(parents)
#load activities.json file and save the data into acts
with open('activities.json', 'r') as f:
    acts = json.load(f)
acts = ast.literal_eval(acts)

#These two parameters are used to make sure there are no more activity need to send
check = 0
flag = 1
while check != flag:
    flag = check
    for mom in pars.keys():
        # Filter Mom who has no registered chldren
        if pars[mom]['age'][0] != '':
            #scan all children who belong same Mom
            for ages in range(len(pars[mom]['age'])):
                tmp_age = pars[mom]['age'][ages]
                #circle activities to find target activity to send
                for i in range(len(acts)):
                    if pars[mom]['act'][ages] == '-1':
                        break
                    if acts[i]['age'][0] == tmp_age:
                        num = pars[mom]['act'][ages]
                        if int(num) != len(acts[i]['activity']):
                            check += 1
                            print "Dear", mom, ": The activity for your child,",pars[mom]['childName'][ages],", is \" ",acts[i]['activity'][int(num)],"\""
                            pars[mom]['act'][ages] = int(pars[mom]['act'][ages]) + 1
                            if int(pars[mom]['act'][ages]) == len(acts[i]['activity']):
                                print "Curriculum complete!"
                                pars[mom]['act'][ages] = '-1'
                            break
