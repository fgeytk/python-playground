def nettoyer_texte(texte):

    ponctuation = ".!?,'"
    for p in ponctuation:
        texte = texte.replace(p, " ")
    return texte.lower()

def compter_mots(texte):
    mots = nettoyer_texte(texte).split()
    freq_dict = {}
    for mot in mots:
        if mot in freq_dict:
            freq_dict[mot] += 1
        else:
            freq_dict[mot] = 1
    return freq_dict

def mot_plus_frequent(freq_dict):
    mot_max = None
    freq_max = 0
    for mot, freq in freq_dict.items():
        if freq > freq_max:
            mot_max, freq_max = mot, freq
    return mot_max, freq_max

texte = ("Au voleur ! au voleur ! à l’assassin ! au meurtrier ! Justice, juste ciel ! "
         "Je suis perdu, je suis assassiné ; on m’a coupé la gorge : on m’a dérobé mon argent. "
         "Qui peut-ce être ? Qu’est-il devenu ? Où est-il ? Où se cache-t-il ? Que ferai-je pour le trouver ? "
         "Où courir ? Où ne pas courir ? N’est-il point là ? n’est-il point ici ? Qui est-ce ? Arrête.")

freq = compter_mots(texte)
print(freq)  
print(mot_plus_frequent(freq))  
