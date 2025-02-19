from copy import deepcopy
import random

def voisins(T,v):
    lignes=len(T)
    colonnes=len(T)
    V=[]
    i,j=v[0],v[1]
    for a in(-1,1):
        if 0<=i+a<lignes:
            if T[i+a][j]==1:
                V.append((i+a,j))
        if 0<=j+a<colonnes:
            if T[i][j+a]==1:
                V.append((i,j+a))
    return V

def parcours( laby , entree, sortie):
    T=deepcopy(laby) 
    p =[]
    v=entree
    T[v[0]][v[1]]=-1
    print(v)
    recherche=True
    while recherche:
        vois=voisins (T,v)
        if vois==[]:
            if p==[]:
                return False
            else:
                v=p.pop()
        else:
            p.append(v)
            v=vois[0]
            T[v[0]][v[1]]=-1
            print(v)
            if v==sortie:
                p.append(v)
                recherche=False
    return p
           

laby=[[0,1,0,0,0,0],
      [0,1,1,1,1,0],
      [0,1,0,1,0,0],
      [0,1,0,1,1,0],
      [0,1,1,0,1,0],
      [0,0,0,0,1,0]]
      
T=deepcopy(laby)
#T[3][2]="hello"
for ligne in laby:
    print(ligne)
    print("----------------")
for ligne in T:
    print(ligne)

ent=(1,1)
sort=(5,4)
print(voisins(T,ent))
#print(parcours(T,ent,sort))