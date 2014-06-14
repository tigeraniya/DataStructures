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
    """
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



if __name__ == '__main__':
    unittest.main()
