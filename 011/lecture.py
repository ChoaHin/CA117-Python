def contains(char, s):
    for c in char:
        if c not in s:
            return False
        s = s.replace(c, "", 1)
    return True

for line in lines:
    [char, s] = line.strip().split()
    print(contains(char, s))
    