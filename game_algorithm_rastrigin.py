import random
import numpy as np
import time

people_num=1000
round=500
talent=20
med_rate=0.01
lb=-5.12
up=5.12




def c_p(x):#能力評估
    cp=10*talent
    for i in range(talent):
        cp+=x[i]**2-10*np.cos(2*np.pi*x[i]) #rastrigin
    return cp

#initial
def initialize():
    people=[]
    for kkk in range(people_num):
        people.append([random.uniform(lb,up) for x in range(talent)])
    return people


#compete each players
def compete_rank(people):
    cpp=[]
    for i in range(len(people)):
        cpp.append(c_p(people[i]))
    cpp_sort= sorted(range(len(cpp)), key = lambda k : cpp[k] ,reverse=False)
    for_50=[people[ll] for ll in cpp_sort[0:len(people)//2]]
    back_50=[people[ll] for ll in cpp_sort[len(people)//2:]]
    return for_50,back_50


#loser update
def loser_deal(for50,back50,learn_rate=0.6,change=0.9,drop=1):
    for o,i in enumerate(back50):
        train=random.random()
        if train<learn_rate:
            ch=random.sample(range(0,talent),talent//2)
            learned_person=random.randint(0,len(for50)//2)
            for k in ch:
                i[k]=for50[learned_person][k]
        elif train>learn_rate or train==learn_rate or train<change:
            random.shuffle(i)
        else:
            i=[random.uniform(lb,up) for x in range(len(i))]          
        back50[o]=i
    return back50

#Uncertainty
def rise_med(competor,reward=1):
    ch=random.sample(range(0,len(competor)),reward)
    for t in range(len(competor[ch[0]])):
        chance=random.random()
        if chance<med_rate:
            competor[ch[0]][t]=random.uniform(lb,up)
    return competor






#find best and test
if __name__ == '__main__':
    start_time = time.perf_counter()
    people=initialize()
    for r in range(round):
        winner,loser=compete_rank(people)
        #print('average=',mean)
        print('round '+str(r+1)+' bestperson:',c_p(winner[0])) 
        loser=loser_deal(winner,loser)
        people=winner+loser
        people=rise_med(people)
    print('Best parameters:',people[0])
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("程式碼執行時間：", execution_time, "秒")