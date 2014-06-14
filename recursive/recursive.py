import os
import sys
import unittest

def uniq(ilst):
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

if __name__ == '__main__':
    unittest.main()
