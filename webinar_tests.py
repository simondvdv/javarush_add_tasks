def power(n):
    if n % 2 == 0:
        def calced(m):
            return m**n
    else:
        def calced(m):
            return m + n
    return calced


a = power(3)
b = power(4)
print(a(5))
print(b(4))
