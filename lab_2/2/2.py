def a(n):
    return (14 * 3**n - 9 * 4**n)

print(a(102) - 7*a(101) + 12*a(100))
print(a(100))