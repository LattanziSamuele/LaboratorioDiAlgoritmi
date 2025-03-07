def lcs_recursive(x, y, m=None, n=None):
    if m is None or n is None:
        m, n = len(x), len(y)

    if m == 0 or n == 0:
        return 0
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs_recursive(x, y, m - 1, n - 1)
    else:
        return max(lcs_recursive(x, y, m, n - 1), lcs_recursive(x, y, m - 1, n))
