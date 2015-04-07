def min_max(l: list) -> tuple:
    minv = l[0]
    maxv = l[0]
    for i in l:
        if i < minv:
            minv = i
        if i > maxv:
            maxv = i
    return minv, maxv


# testing code
liste = [3, 2, 1, 4, 5, 6, 9, 8, 7]
(a, b) = min_max(liste)
print("min:", a)
print("max:", b)

# extract single value from tuple
c = min_max(liste)[0]

# swap
a, b = b, a