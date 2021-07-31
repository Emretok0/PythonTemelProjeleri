liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# liste = [[1,2,[3,[4,[5,6]]],7],[8,9]]
newList = []


def apply1(liste):
    for i in liste:
        if (type(i)==list):
            apply2(i)
        else:
            newList.append(i)

def apply2(liste):
    for i in liste:
        if (type(i)==list):
            apply2(i)
        else:
            newList.append(i)
apply1(liste)
print(newList)