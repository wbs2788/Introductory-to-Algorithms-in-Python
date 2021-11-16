'''
Author: wbs2788
Date: 2021-11-16 23:24:31
LastEditTime: 2021-11-17 00:34:35
LastEditors: wbs2788
Description:  fft
'''
from cmath import pi, exp

def fft(x):
    # x is a list of complex numbers
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [exp(i * 2j * pi / N) * odd[i] for i in range(N//2)]
    return [even[i] + T[i] for i in range(N//2)] + [even[i] - T[i] for i in range(N//2)]

def ifft(x):
    f = fft(x)
    ans = f[1:len(x)]
    ans.append(f[0])
    return [i / len(x) for i in ans[::-1]]

a = [1, 2, 0, 0]
b = [3, 4, 0, 0]

print(ifft([i*j for i, j in zip(fft(a), fft(b))]))