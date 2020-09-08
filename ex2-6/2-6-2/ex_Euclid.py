import sys
sys.setrecursionlimit(1000000) 
a, b =map(int, input().split())

# 拡張ユークリッド互除法
# gcd(a,b) と ax + by = gcd(a,b) の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


from typing import Tuple
def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
print(xgcd(10,6))
"""
m1 = 10
m2 = 6
gcd, x, y = egcd(m1, m2)

# 10で割ると1余り6で割ると3余る数を求める
b1 = 1
b2 = 3
s = (b2 - b1) // gcd  # これは必ず割り切れる
ans = b1 + m1 * s * x
print(ans)
"""