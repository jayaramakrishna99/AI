import random

import numpy as np


def m(w, h):
    s = []
    w_x = random.randrange(2, w)
    g_x = random.randrange(2, w)
    w_y = random.randrange(2, h)
    g_y = random.randrange(2, h)
    # print(w_x)
    while w_x == g_x and w_y == g_y:
        g_x = random.randrange(2, w)
        g_y = random.randrange(2, h)
    for i in range(h):
        l1 = []
        for j in range(w):
            if (i == 0 or i == 1) and (j == 0 or j == 1):
                l1.append(0)
            elif i == w_x and j == w_y:
                l1.append(2)
            elif i == g_x and j == g_y:
                l1.append(3)
            elif ((i == w_x + 1 or i == w_x - 1) and j == w_y) or ((j == w_y + 1 or j == w_y - 1) and i == w_x):
                l1.append(0)
            else:
                if random.random() <= 0.25:
                    l1.append(1)
                else:
                    l1.append(0)
        s.append(l1)
    a = np.array([])
    a = np.append(a, s)
    print(s)
    a = a.reshape(4,4)
    # s['c_p'] = [0, 0]
    print(a)


m(4, 4)
# def