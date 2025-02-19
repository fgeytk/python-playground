#Replit Lycee
#!/usr/bin/env python3
adresseTexte = input("Entrez une adresse ip et le masque svp: ")
d,m= adresseTexte.split("/")
a,b,c,d =d.split(".")
m=int(m)
a=int(a)
b=int(b)
c=int(c)
d=int(d)
def liste_octet(n):
    """
    retourne la liste des bits de l'octet n en écriture décimale
    Exemple :
    >>> liste_octet(129)
    ['1', '0', '0', '0', '0', '0', '0', '1']
    """
    nbin=bin(n).replace('0b','00000000')
    nbin=nbin[len(nbin)-8:len(nbin)]
    nbin_liste=[]
    for i in range(8):
        nbin_liste.append(nbin[i])
    return nbin_liste

def fonction_ET(o1,o2):
    """
    retourne l'octet en écriture décimale
    résultat l'opération logique o1 ET o2
    o1 et o2 sont des octets en écriture décimale
    Exemple :
    >>> fonction_ET(127,254)
    126
    """
    o=[]
    for i in range(8):
        if int(liste_octet(o1)[i])*int(liste_octet(o2)[i])==1:
            o.append(1)
        else:
            o.append(0)
    d=0
    for i in range (8):
        d=d+2**(7-i)*o[i]
    return d

def fonction_OU(o1,o2):
    """
    retourne l'octet en écriture décimale
    résultat l'opération logique o1 OU o2
    o1 et o2 sont des octets en écriture décimale
    Exemple :
    >>> fonction_OU(127,254)
    255
    """
    o=[]
    for i in range(8):
        if int(liste_octet(o1)[i])+int(liste_octet(o2)[i])>0:
            o.append(1)
        else:
            o.append(0)
    d=0
    for i in range (8):
        d=d+2**(7-i)*o[i]
    return d

 
def masque(m,a,b,c,d):
  amasque=int(0) #Definition des varianbles du masque 
  bmasque=int(0)
  cmasque=int(0)
  dmasque=int(0)
  a=int(a)
  b=int(b)
  c=int(c)
  d=int(d)
  indice = 1
  indiceOctet = 0
  for i in range (m): #fonction de création du masque (j'ai été aider pour cette fonction)
    
    if i <8:
      amasque+=128/indice
      
    elif i>=8 and i<16:
      bmasque+=128/indice
    elif i>=16 and i<24:
      cmasque+=128/indice
    else:
      dmasque+=128/indice
    
    indice *= 2
    indiceOctet += 1

    if indiceOctet == 8:
      indice = 1
      indiceOctet = 0
  amasque=int(amasque)
  bmasque=int(bmasque)
  cmasque=int(cmasque)
  dmasque=int(dmasque)
  print("Le masque de votre sous réseau est:",amasque,".",bmasque,".",cmasque,".",dmasque)   
  print("L'adresse de votre sous réseau:",fonction_ET(amasque,a),".",fonction_ET(bmasque,b),".",fonction_ET(cmasque,c),".",fonction_ET(dmasque,d))  

  a2=0
  b2=0
  c2=0
  d2=0
  indice = 1
  indiceOctet = 0
  # 
  for i in range(m):
    if a-(128/indice) >=0 and i<8:
      a2+=128/indice
      a=a-(128/indice)
    

    if b-(128/indice)>=0 and i>=8 and i<16:
      b2+=128/indice
      b=b-(128/indice)

    
    if c-128/indice>=0 and i>=16 and i<24:
      c2+=128/indice
      c=c-(128/indice)

    
    if d-128/indice>=0 and i>=24:
      d2+=128/indice
      d=d-(128/indice)


    indice *= 2
    indiceOctet += 1
    
    if indiceOctet == 8:
      indice = 1
      indiceOctet = 0
      
  indiceOctet = 0
  for i in range(32-m):
    if i>=24:
      a2+= 2**indiceOctet

    if b-2**indiceOctet>=0 and i>=16 and i<24:
      b2+=2**indiceOctet
    
    if i>=8 and i<16:
      c2+=2**indiceOctet
    
    if i<8:
      d2+=2**indiceOctet
      
    indiceOctet += 1
    
    if indiceOctet == 8:
      indiceOctet = 0
  a2=int(a2)
  b2=int(b2)
  c2=int(c2)
  d2=int(d2)
  print("L'adresse broadcast est: ",a2,".",b2,".",c2,".",d2)
    

def nombremachine(m): #donne le nombre de amachine adresable
  m=32-m
  print("Cela fait",(2**m)," machine")


masque(m,a,b,c,d) 
print(nombremachine(m))
