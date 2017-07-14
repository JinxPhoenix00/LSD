karty = []
body.append(int(input()))
dalsi = input()
while dalsi != "0":
    karty.append(dalsi)
    dalsi = input()
# print(karty)
karty.sort()
pocet = 0

def jedna():
    for i, prvek in enumerate(karty):
        if prvek == "zl":
            if i+1 == len(karty):
                global pocet
                pocet = 3
                break
            elif karty[i+1] == "zl":
                break
            else:
                global pocet
                pocet = 3


def pet():
    print()
jedna()
body = body + pocet
pocet = 0
pet()
body = body + pocet
pocet = 0
print(body)
