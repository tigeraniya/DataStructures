
import ctypes

coin = [0]

class DA(object):
    
    def __init__(self):
        self._capacity = 1
        self._n = 0
        self._A = self.make_array(self._capacity)

    def __len__(self,):
        return self._n

    def __getitem__(self,k):
        if 0 <= k < self._n:
            return self._A[k]
        else:
            raise IndexError

    def __setitem__(self,k,obj):
        if 0 <= k < self._n:
            self._A[k] = obj
        else:
            raise IndexError
    
    def append(self,obj):
        if self._n == self._capacity:
            self.resize()
        self._A[self._n] = obj
        coin[0] +=1
        print coin[0]
        self._n += 1

    def make_array(self,n):
        return (n * ctypes.py_object)()

    def resize(self):
        _B = self.make_array(self._capacity * 2)
        for i in range(self._n):
            _B[i]=self._A[i]
            coin[0] +=1
            print coin[0]
        self._A = _B
        self._capacity = self._capacity * 2

    def __str__(self):
        return str([i for i in self._A])


d = DA()
for i in range(16):
    d.append(i)
print d
