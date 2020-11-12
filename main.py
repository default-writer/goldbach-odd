"""
Every odd number not being a prime number is a sum of a prime number and a double of natural number in power of two 
9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

... until it mets 5777

"""

from datetime import datetime

start = datetime.now()

p = [2]
c = []

found = True
i = 3
while found:
    if not ((i > 10) and (i % 10 == 5)):
        for j in p:
            if not found:
                break
            if j * j - 1 > i:
                p.append(i)
                break
            if i % j == 0:
                c.append(i)
                found = False
                for pj in p:
                    if found:
                        break
                    if i > pj and (i - pj) % 2 == 0:
                        k = 1
                        n = 1
                        while True:
                            if (i - pj) / 2 < k:
                                break
                            if (i - pj) / 2 == k:
                                found = True
                                break
                            k += 2*n + 1
                            n += 1
                if not found:
                    print(f"{i}")
                break
        else:
            p.append(i)
    i += 2

print((datetime.now() - start).__str__())
