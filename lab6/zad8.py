def ciag(liczby, n):
    return ((liczby[0] + liczby[n]) / 2) * n

liczby = [4, 5, 7, 9, 14, 17]
print(ciag(liczby, 5))