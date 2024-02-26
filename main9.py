a = "moveMENT"
resulte = ""
resulte2 = ""
n1 = a.casefold()
m1 = a.upper()
for x in a:
    if x not in n1:
        resulte += x
    if x not in m1:
        resulte2+= x
print(resulte+resulte2)

