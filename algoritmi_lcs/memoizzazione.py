def lcs_memoized(x, y):
    m, n = len(x), len(y)

    table = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    return lcs_memoized_aux(x, y, m, n, table)


def lcs_memoized_aux(x, y, m, n, table):
    if m == 0 or n == 0:
        return 0

    if table[m][n] != -1:
        return table[m][n]

    if x[m - 1] == y[n - 1]:
        table[m][n] = 1 + lcs_memoized_aux(x, y, m - 1, n - 1, table)
    else:
        table[m][n] = max(lcs_memoized_aux(x, y, m, n - 1, table), lcs_memoized_aux(x, y, m - 1, n, table))

    return table[m][n]
