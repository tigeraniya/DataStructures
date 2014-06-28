import os
import sys
import unittest

def uniq(ilst):
    """
    non-recursive 
    return True if all elements are unique in list
    """
    l = len(ilst)
    for i in range(l):
        for j in range(i+1,l):
            if ilst[i] == ilst[j]:
                return False
    return True

class TestUniq(unittest.TestCase):
    def test_uniq(self):
        self.assertEqual(True,uniq([1,2,3]))
        self.assertEqual(True,uniq([1]))
        self.assertEqual(False,uniq([1,2,1]))
        self.assertEqual(False,uniq([9,1,2,1]))

def rec_uniq(ilst,n):
    """C 4.11
    recursive : first checks nth element uniqueness in n-1 elements,
                then n-1th element uniqueness in n-2 elements
    """
    #print ilst,n
    if n <= 1:
        return True
    else:
        if not runiq(ilst,n,n-1):
            return False
        else:
            return rec_uniq(ilst,n-1)

def runiq(ilst,num,n):
    """
    checks num-th element is not in first n elements
    """
    #print num,n
    if n < 1:
        return True
    else:
        if ilst[num-1] == ilst[n-1]:
            return False
        else:
            return runiq(ilst,num,n-1)

class TestRuniq(unittest.TestCase):
    def test_runiq(self):
        self.assertEqual(True,rec_uniq([1,2,3],3))
        self.assertEqual(True,rec_uniq([1],1))
        self.assertEqual(False,rec_uniq([1,2,3,1],4))
        self.assertEqual(False,rec_uniq([1,2,1,3,5],4))

def rprod(m,n):
    if n <= 0:
        return 0
    else:
        return m + product(m,n-1)
    
def product(m,n):
    """C 4.12 
    recursive:compute product of two positive numbers using only +/- 
    """
    if m > n:  # if n > m then we are calling functions more then needed
        return rprod(m,n)
    else:
        return rprod(n,m)

class TestProduct(unittest.TestCase):
    def test_product(self):
        self.assertEqual(5,product(5,1))
        self.assertEqual(0,product(5,0))
        self.assertEqual(22,product(2,11))
        self.assertEqual(0,product(0,5))

def thanoi(src,hlp,dst,n):
    if n > 0 :
        moves = thanoi(src,dst,hlp,n-1) # move from source to helper n-1 tiles using destination
        moves += 1 
        dst[0].append(src[0].pop()) # after we have largest tile on source , move it to destination
        #print [[str((k,i[0])).ljust(20,' ') for i in  src,hlp,dst if i[1] == k] for k in ["src","hlp","dst"]]
        moves += thanoi(hlp,src,dst,n-1) # now move n -1 tiles from helper to destination using source
        return moves
    else:
        return 0

def towers_of_hanoi(src,hlp,dst):
    """C 4.14
    recursive : towers of hanoi
    src,hlp,dst strings are attached on to tuple to know which tower are we on really

    """
    return thanoi((src,"src"),(hlp,"hlp"),(dst,"dst"),len(src))
    
class TestHanoi(unittest.TestCase):
    def test_hanoi(self):
        self.assertEqual(7,towers_of_hanoi([3,2,1],[],[]))        

def subsets(ilst,n):
    """C 4.15
    get all subsets of a set without repitition
    """
    result = [[]]
    for x in ilst:
        #print x,result
        result.extend([[x]+subset for subset in result])
    return result

def rsubsets(ilst,n):
    """C 4.15
    recursive : get all subsets of a set
    """
    result = []
    if (n>0):
        tresult = rsubsets(ilst,n-1)
        return tresult + [sub + [n] for sub in tresult]
    else:
        result.append([])
    return result

class TestSubSet(unittest.TestCase):
    def test_subset(self):
        self.assertIn([],subsets([1,2],2))
        self.assertIn([],rsubsets([1,2],2))

def revstr(istr,s,e):
    if s > e-1:
        return ''
    elif s == e-1:
        return istr[s]
    else:
        return istr[e-1] + revstr(istr,s+1,e-1) + istr[s]
           

def reverse_string(istr):
    """C 4.16 
    recursive :reverse a string
    """
    return revstr(istr,0,len(istr))

class TestRevStr(unittest.TestCase):
    def test_revstr(self):
        self.assertEqual("idnhem",reverse_string("mehndi"))
        self.assertEqual("iagnhem",reverse_string("mehngai"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        self.assertEqual("im",reverse_string("mi"))

vow = ['a','e','i','o','u']

def tletter(istr,n):
    tmp_ret = [0,0]
    if n <= 0:
        return tmp_ret
    else:
        tmp_iret = tletter(istr,n-1)
        if istr[n-1] in vow:
            tmp_iret[0] +=1
        else:
            tmp_iret[1] += 1
        return tmp_iret
    

def letter_type(word):
    ret =  tletter(word,len(word))
    if ret[0] > ret[1]:
        print "more vowels"
    elif ret[0] == ret[1]:
        print "same nos"
    else:
        print "more consonents"
      
class Test_LetterType(unittest.TestCase):
    
    def test_letter_type(self):
        self.assertEqual([2,1],tletter("aba",3))
        self.assertEqual([2,2],tletter("baba",4))
        
is_even = lambda x : x % 2 == 0
is_odd = lambda x : x % 2 != 0

def _even_odd_sort(ilst,n,mark):
    """
    """
    if n-2 < 0:
        return ilst
    else: 
        if is_even(ilst[n-1]) and is_odd(ilst[n-2]):
            ilst[mark[0]-1],ilst[n-2] = ilst[n-2],ilst[mark[0]-1]
            mark[0] -= 1
    return _even_odd_sort(ilst,n-1,mark)
 
def even_odd_sort(ilst):
    l = len(ilst)
    return _even_odd_sort(ilst,l,[l])
class TestEvenOddSort(unittest.TestCase):
    
    def test_even_odd(self):
        self.assertEqual([2,2,4,1,1,3],even_odd_sort([1,2,1,2,3,4]))
        self.assertEqual([4,2,2,9,1,1,3],even_odd_sort([9,1,2,1,2,3,4]))

if __name__ == '__main__':
    unittest.main()
