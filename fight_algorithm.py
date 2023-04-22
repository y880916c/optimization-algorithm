import random
import numpy as np

people_num=1000
round=500
talent=7

def c_p(a):#能力評估
    cp=a[0]+a[1]-a[2]+a[3]-a[4]+a[5]-a[6]*8 #1 1 0 1 0 1 8
    return cp

def compete_rank(people):
    cpp=[]
    for i in range(len(people)):
        cpp.append(c_p(people[i]))
    cpp_sort= sorted(range(len(cpp)), key = lambda k : cpp[k] ,reverse=True)
    for_50=[people[ll] for ll in cpp_sort[0:len(people)//2]]
    back_50=[people[ll] for ll in cpp_sort[len(people)//2:]]
    return for_50,back_50,np.mean(cpp[0:people_num//2])

def loser_deal(for50,back50,learn_rate=0.6,change=0.9,drop=1):
    for o,i in enumerate(back50):
        train=random.random()
        if train<learn_rate:
            #print(1)
            ch=random.sample(range(0,5),5//2)
            learned_person=random.randint(0,len(for50)//2)
            for k in ch:
                #print(i,k,ch,learned_person)
                i[k]=for50[learned_person][k]
        elif train>learn_rate or train==learn_rate or train<change:
            #print(2)
            random.shuffle(i)
        else:
            #print(3)
            i=[random.random() for x in range(len(i))]          
        back50[o]=i
    return back50

def rise_med(competor,reward=1):
    ch=random.sample(range(0,len(competor)),reward)
    for t in range(len(competor[ch[0]])):
        chance=random.random()
        if chance<0.01:
            competor[ch[0]][t]=random.random()
    return competor

#initial
people=[]
for kkk in range(people_num):
    people.append([random.random() for x in range(talent)])

#find best
for r in range(round):
    winner,loser,mean=compete_rank(people)
    print('round '+str(r)+' bestperson',c_p(winner[0]))
    print('average=',mean)
    loser=loser_deal(winner,loser)
    people=winner+loser
    people=rise_med(people)