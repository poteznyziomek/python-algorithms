import math, random

def to_base(m, N=2):
    mm = []
    net = 0
    aa = m % N
    mm.append(aa)
    while m > 0 and net < 1000:
      net += 1
      m = int((m - aa) / N)
      aa = m % N
      mm.append(aa)
    return mm[:-1]

def adbin(a, b, n):
    #n = len(a) + 1
    c = [0 for i in range(n+1)]
    memory = 0
    for i in range(n):
      c[i] = (a[i] + b[i] + memory) % 2
      memory = math.floor((a[i] + b[i] + memory) / 2)
    c[n] = memory
    return c
