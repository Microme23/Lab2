def fun2 (n):
    S = 0
    for i in range (1, n+1):
        S = (S + (i+1)/i)
    return S