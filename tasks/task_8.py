"""
таблица уможения
"""

import numpy as np

list = np.zeros((9, 9))
for i in range(9):
    for n in range(9):
        list[n][i] = (i + 1) * (n + 1)
print(list)
