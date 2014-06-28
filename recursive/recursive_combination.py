# generate combination
"""
to find a change for given amount from given  coins

"""

def find_changes(amount,coins):
    if amount < 0:
        return [] #no combination found 
    if amount == 0 :
        return [[]] #combination valid as amount is 0 coins will be added via returns
    all_changes = [] #all combos collect here
    for last_coin_used in coins:
        combos = find_changes(amount - last_coin_used,coins)
        for combo in combos:
            combo.append(last_coin_used)
            all_changes.append(combo)
    return all_changes

print find_changes(4,[1,2,3,4])
