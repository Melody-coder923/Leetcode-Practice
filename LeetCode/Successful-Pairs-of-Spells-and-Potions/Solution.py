potions.sort()
return (len(potions) - bisect_left(potions, success, key=lambda p: p * s) for s in spells)