import random

# Experience (thought this would be cool to allow hp and atk level unlocks as well as determine the dmg that's taken)
def xp():
    experience = 0

    return experience

# Health sets depending on XP (hopefully)
def hp(i):
    health = 0

    if i == 0:
        health += 10
       
    return health

# Attack
def atk(xp):
    pass

# Damage
def dmg(xp):
    pass

# Dice throw (two dice)
def throw():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
   
    print d1 # Printing d1 and d2 for debugging
    print d2
 
    total = d1 + d2
    return total
    
print throw()
print xp()
print hp(xp)
