bos = []
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def duzlestir(x):
    for i in x:
        if isinstance(i, list):
            duzlestir(i)
        else:
            bos.append(i)

duzlestir(liste)
print(bos)
