#Replit Lycee

def fusion(gauche, droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])            
            index_droite += 1
    if gauche:  # si la liste gauche n'est pas vide
        resultat.extend(gauche[index_gauche:])
    if droite:  # si la liste droite n'est pas vide
        resultat.extend(droite[index_droite:])
        print('fusioner',gauche,'+' ,droite)
        return resultat


def tri_fusion(m):
    if len(m) <= 1:
      print('regner',m)  
      return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    print('diviser',m,'=',gauche,'+',droite)
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))
