P = int(input())
N = int(input())

def calc_times_n(N: int, x: int):
    #Nのz乗
    x_bits= bin(x)[2:][::-1]
    ans = 1
    bit_idx = 0
    for bit in x_bits:
        if int(bit):
            ans *= N ** (1 << bit_idx)
        bit_idx += 1
    return ans

# ===========引用
def binary(n):
    return bin(n)[2:]

def pow_by_binary(a, x, n): # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y

#1. p が素数のとき、x^n % p = x^(n%(p-1)) % p
#2. p-1 > c > 1 のとき、x^n+y^n≡c (mod p) を満たす個数は０または x^n+y^n≡1 (mod p) を満たす個数に等しい。
# ============

ans = 0
for z in range(P):
    Z = calc_times_n(z, N)
    for x in range(P):
        X = calc_times_n(x, N) % P
        for y in range(P):
            Y = calc_times_n(y, N) % P

            if (X + Y) % P == Z % P:
                ans += 1
print(ans)