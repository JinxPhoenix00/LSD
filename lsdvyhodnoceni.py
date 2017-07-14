karty = []
body = []
dalsi = input()
while dalsi != "0":
    karty.append(dalsi)
    dalsi = input()
# print(karty)
karty.sort()


def jedna():
    pocet = 3
    for i, prvek in enumerate(karty):
        if prvek == "zl":
            if i+1 == len(karty):
                global body
                pocet.append(body)
                break
            elif karty[i+1] == "zl":
                break
            else:
                global body
                pocet.append(body)


def pet():
    print()

def sestnact():
    body.append(int(2))

jedna()

pet()
sestnact()
print(body)
