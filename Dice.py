import random
import numpy as np

def rollDice(rolls, sides):
    result=np.arange(rolls)
    count=0
    while count < rolls:
        result[count]=random.randint(1, sides)
        count+=1
    return result

def getStat():
    a = rollDice(4, 6)
    a = np.delete(a, a.argmin())
    result = np.sum(a)
    if result<=8:
        result=8
    return result

def getHitPoints(level, sides):
    a = np.arange(level)
    sum=sides
    a[0]=sides
    count=1
    while count<level:
        a[count]=random.randint(sides/2, sides)
        sum+=a[count]
        count+=1
    print(a)
    return sum

def getStats():
    result=np.arange(6)
    count=0
    while count<6:
        result[count]=getStat()
        count+=1
    return result

def getStatScore(stat):
    if(stat>=0 and stat<9):
        return 0
    if(stat==9):
        return 1
    if(stat==10):
        return 2
    if(stat==11):
        return 3
    if(stat==12):
        return 4
    if(stat==13):
        return 5
    if(stat==14):
        return 7
    if(stat==15):
        return 9
    if(stat==16):
        return 11
    if(stat==17):
        return 13
    if(stat==18):
        return 15

def scoreStats(stats):
    sum=0
    for num in stats:
        sum+=getStatScore(num)
    return sum

def generateStats(targetScore, targetNumber):
    count=0
    while count < targetNumber:
        result=getStats()
        score=scoreStats(result)
        if score==targetScore:
            print(np.sort(result)[::-1])
            count+=1

#%%

a=[15, 14, 13, 12, 10, 8]

print(scoreStats(a))

#%%

generateStats(32, 20)


#%%

a=getHitPoints(3, 10)
print(a)
# %%
a=getHitPoints(3, 6)
print(a)

# %%
