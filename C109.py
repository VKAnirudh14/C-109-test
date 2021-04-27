import statistics
import random
import plotly.figure_factory as ff 



diceResult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)

mean=sum(diceResult)/len(diceResult)
print(mean)

standardDeviation=statistics.stdev(diceResult)
print(standardDeviation)

median=statistics.median(diceResult)
print(median)

mode=statistics.mode(diceResult)
print(mode)

fig=ff.create_distplot([diceResult],["Results"],show_hist=False)
fig.show()

