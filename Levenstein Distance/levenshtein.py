import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def levensthein_razdalja(s1, s2, spremembe=False):
    """
    Računanje Levenshteinove razdalje med s1 in s2.
    
    Argumenti:
        s1, s2: Stringa katera primerjamo med seboj
        spremembe: Default=False. Če postavimo na True nam izpiše spremembe. 
        
    Vrne:
        Najmanjšo vrednost sprememb med dvema string-oma, oz. najbolj spodnjo desno številko matrike.
        matriko
        najkrajšo pot 
    """
     
    m = len(s1)
    n = len(s2)

    # ustvarite matriko za shranjevanje razdalj
    razdalja = np.zeros((m+1,n+1))

    # inicializiramo prvo vrstico in stolpec matrike
    for i in range(m + 1):
        razdalja[i,0] = i
    for j in range(n + 1):
        razdalja[0,j] = j

    # izračunamo razdaljo 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                razdalja[i,j] = razdalja[i - 1,j - 1]
            else:
                razdalja[i,j] = min(razdalja[i - 1,j], razdalja[i,j - 1], razdalja[i - 1,j - 1]) + 1
    
    # Inicializiramo pot 
    path = []
    pathOperacije = []
    # Backtrack-amo da najdemo pravo pot
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            path.append((i, j))
            pathOperacije.append('enačenje')
            i -= 1
            j -= 1
        else:
            if razdalja[i-1][j] < razdalja[i][j-1]:
                if razdalja[i-1][j] < razdalja[i-1][j-1]:
                    path.append((i, j))
                    pathOperacije.append('vrivanje')
                    i -= 1
                else:
                    path.append((i, j))
                    pathOperacije.append('zamenjava')
                    i -= 1
                    j -= 1
            else:
                if razdalja[i][j-1] < razdalja[i-1][j-1]:
                    path.append((i, j))
                    pathOperacije.append('brisanje')
                    j -= 1
                else:
                    path.append((i, j))
                    pathOperacije.append('zamenjava')
                    i -= 1
                    j -= 1
            
    if spremembe == True:
        print("Operacije:", pathOperacije[::-1])

    
    matrika = np.zeros((m + 1, n + 1))
    for i in range(m + 1):
        matrika[i, 0] = i
    for j in range(n + 1):
        matrika[0, j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            matrika[i, j] = min(matrika[i - 1, j] + 1, matrika[i, j - 1] + 1, matrika[i - 1, j - 1] + cost)
    
        
    return razdalja[m][n], matrika, path
