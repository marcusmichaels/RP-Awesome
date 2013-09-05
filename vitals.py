import random

# Health
def hp():
    pass

# Attack
def atk():
    pass

# Damage
def dmg():
    pass

# Experience (thought this would be cool to allow level unlocks)
def xp():
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
