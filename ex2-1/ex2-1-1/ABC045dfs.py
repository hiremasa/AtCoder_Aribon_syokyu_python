S = input()

def dfs(i, f):
    if i == len(S) - 1:
        return sum(list(map(int, f.split("+"))))

    else:

        return dfs(i + 1, f + "+" + S[i + 1]) + dfs(i + 1, f + S[i + 1])

print(dfs(0, S[0]))