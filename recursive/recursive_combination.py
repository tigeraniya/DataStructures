# generate combination


def find_changes(n,coins):
    if n < 0:
        return []
    if n == 0 :
        return [[]]
    all_changes = []
    for last_coin_used in coins:
        combos = find_changes(n - last_coin_used,coins)
        for combo in combos:
            combo.append(last_coin_used)
            all_changes.append(combo)
    return all_changes

print find_changes(4,[1,2,3,4])


def recursive_sum(tgt,ilst):
    if n <
