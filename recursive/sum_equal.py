"""
Suppose you are given an n-element sequence, S, containing distinct in-
tegers that are listed in increasing order. Given a number k, describe a
recursive algorithm to find two integers in S that sum to k, if such a pair
exists. What is the running time of your algorithm?
"""

import unittest

def sumequal(isum,ilst):
    if isum < 0:
        return []
    if isum == 0:
        return [[]]
    all_sum_combos = []
    for last_num in ilst:
        combos = sumequal(isum - last_num,ilst)
        for combo in combos:
            combo.append(last_num)
            all_sum_combos.append(combo)
    return all_sum_combos

def nonrecsum(isum,ilst):
    ilst = sorted(ilst)
    lenl = len(ilst)
    sols = []
    for i1 in range(lenl):
        if ilst[i1] > isum:
            continue
        else:
            for i2 in range(i1,lenl):
                print ilst[i1],ilst[i2]

                tsum = ilst[i1] + ilst[i2]
                if tsum == isum :
                    sols.append((ilst[i1],ilst[i2]))
                elif tsum > isum:
                    continue
    return sols


def _recsum(isum,ilst,n,m):
    if n == 0:
        return []    
    all_combos = []
    
    print n,m,ilst[n-1],ilst[m-1]
    if isum == ilst[m-1] + ilst[n-1] and m != 0:
        print "hit"
        all_combos.append((ilst[m-1],ilst[n-1]))
    if m == 0 :
        all_combos += _recsum(isum ,ilst,n-1,n-2)
    else:
        all_combos += _recsum(isum ,ilst,n,m-1)
    return all_combos

def recsum(isum,ilst):
    ll = len(ilst)
    return _recsum(isum,ilst,ll,ll-1) 

#print sumequal(6,[2,3,4])
#print sumequal(20,[20])
#print nonrecsum(6,[2,3,4])
#print nonrecsum(20,list(range(1,20)))

print recsum(20,[1,5,10,10,15])
print recsum(5,[1,2,3,4])
