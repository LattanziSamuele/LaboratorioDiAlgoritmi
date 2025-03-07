def generate_subsequences(s, index=0, current=""):
    if index == len(s):
        return [current] if current else []
    exclude = generate_subsequences(s, index + 1, current)
    include = generate_subsequences(s, index + 1, current + s[index])
    return exclude + include


def is_subsequence(sub, s):
    it = iter(s)
    return all(char in it for char in sub)


def lcs_brute_force(x, y):
    subsequences_x = generate_subsequences(x)
    longest = ""
    for sub in subsequences_x:
        if is_subsequence(sub, y) and len(sub) > len(longest):
            longest = sub
    return len(longest)
