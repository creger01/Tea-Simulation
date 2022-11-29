class teaMug:
    """Represents how much tea is in the mug."""

myTea = teaMug()

myTea.color = "brown"
myTea.size = "15 oz"               #how big the cup is
myTea.shape = "diamond"
myTea.amount = 15                   #how much tea is in the cup


import math
def tea_drinking_simulation(t, minutes):        #t=myTea
    leftover = t.amount - 2*minutes        #takes 2 minutes to drink 1oz
    print(leftover)

tea_drinking_simulation(myTea, 6)
