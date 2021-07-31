# liste = [[1,2],[3,4],[5,[6,7,8],9,10]]
liste = [[1, 2], [3, 4], [5, 6, 7]]
liste.reverse()

def rev(liste):
    for i in liste:
        if (type(i)==list):
            i.reverse()
            rev2(i)


def rev2(liste):
    for i in liste:
        if (type(i)==list):
            i.reverse()
            rev2(i)

rev(liste)
print(liste)
