import random

# Experience (thought this would be cool to allow hp and atk level unlocks as well as determine the dmg that's taken)
def xp():
    experience = 0

    return experience

# Health sets depending on XP (hopefully)
def hp():
    health = 0

    if xp() == 0:
        health += 10
    elif xp() <= 200:
        health += 500
    else:
        health += 1000
       
    return health

# Attack
def atk():
    pass

# Damage
def dmg():
    pass

# Dice throw (two dice)
def throw():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
   
    total = d1 + d2
    return total
    
print "\nYou have %s health and have thrown a %s, your experience is currently at %s\n" % (hp(), throw(), xp())
