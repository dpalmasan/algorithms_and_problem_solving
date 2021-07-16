def lcs_length(x, y):
    m = len(x)
    n = len(y)

    c = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        c[i][0] = 0
    for j in range(n):
        c[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]

    return c[m][n]


def memoized_lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            c[i][j] = -1

    return memoized_lcs_aux(x, y, c, m, n)


def memoized_lcs_aux(x, y, c, i, j):
    if c[i][j] > -1:
        return c[i][j]
    else:
        if i == 0 or j == 0:
            cc = 0
        elif x[i - 1] == y[j - 1]:
            cc = memoized_lcs_aux(x, y, c, i - 1, j - 1) + 1
        else:
            cc = max(
                memoized_lcs_aux(x, y, c, i, j - 1),
                memoized_lcs_aux(x, y, c, i - 1, j),
            )

    c[i][j] = cc
    return cc


print(lcs_length("ABCBDAB", "BDCABA"))
print(memoized_lcs("ABCBDAB", "BDCABA"))
