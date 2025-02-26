import timeit


def tri_fufu(liste):
    l = len(liste)
    gauche = []
    droite = []
    if l <= 1:
        return liste
    pivot = liste[l // 2]  # Pivot au milieu
    for i in range(l):
        if liste[i] < pivot:
            gauche.append(liste[i])
        elif liste[i] > pivot:
            droite.append(liste[i])
    return tri_fufu(gauche) + [pivot] + tri_fufu(droite) #transforme le pivot en liste sinon erreur
liste_test = [10,54,85,963,1,4,47,25,61,397,1000,0]
#print(tri_fufu(liste_test))
# Chat GPT
temps_execution = timeit.Timer(lambda: tri_fufu(liste_test)).timeit(number=10)
print(f"Temps d'exécution pour 10 exécutions : {temps_execution:.6f} secondes")
