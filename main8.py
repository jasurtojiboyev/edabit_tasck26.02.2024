m = "abCBA"
v = m.casefold()
c = m.upper()
resulte = 0
resulte2 = 0
for x in m:
    if x in c:
        resulte += 1
    else:
        resulte2 += 1
print(resulte)


