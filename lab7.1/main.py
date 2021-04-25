import numpy as np
from math import *
# Zad 1
a = np.array([2, 3, 4])
b = np.array([4, 5, 6])
c = a * b
print(f'Macierz a: {a}\nMacierz b: {b}\nPo wykonaniu operacji mnozenia: {c}')

# Zad 2


d = np.array([[2, 3, 5], [6, 7, 2], [3, 8, 9]])
e = np.array([[2, 3, 5, 6], [6, 6, 7, 2], [3, 7, 8, 9], [1, 1, 4, 6]])


# Zad 3

a = np.array([2, 3, 4])
b = np.array([[4],
              [5],
              [6]])
c = np.dot(a, b)
print(f'Macierz a: {a}\nMacierz b: {b}\nIloczyn macierzy: {c}')

# Zad 4

a = np.array([2, 3, 4])
print(f'Typ {a} --> {a.dtype}')
b = np.array([5, 2.1, 5.3])
print(f'Typ {b} --> {b.dtype}')
c = a * b
print(f'Macierz a: {a}\nMacierz b: {b}\nPo wykonaniu operacji mnozenia: {c}\nTyp po wykonaniu mnozenia: --> {c.dtype}')

# Zad 5

a = np.sin(np.array([[45, 60, 30],
              [90, 0, 30]]))
print(a)

# Zad 6