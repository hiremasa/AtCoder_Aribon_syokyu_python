"""
import copy
input_S =list(raw_input())
T = ""
reversed_S = copy.deepcopy(input_S)

reversed_S.reverse()

while(len(input_S)> 0):
    if input_S < reversed_S:
        T += input_S[0]
        input_S = input_S[1:]
        reversed_S= reversed_S[:-1]

    else:
        T += reversed_S[0]
        input_S = input_S[:-1]
        reversed_S= reversed_S[1:]
print T
"""

from collections import deque
N=int(input())
S=deque(input())
T=""
S_rev=S.copy()
S_rev.reverse()

while len(S)>0:
	if S<S_rev:
		T+=S.popleft()
		S_rev.pop()
	else:
		T+=S_rev.popleft()
		S.pop()
print(T[2:])
