
from random import shuffle
import time



class JeuDeCartes(object):

    def __init__(self,compteur):
      self.carte = []  # Liste vide à remplir
      self.compteur=compteur
      if compteur==0:
        """Construction du jeu de carte"""
        
        """Simulation d'un jeu de 52 cartes"""
        # Valeur des cartes
        self.valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
        # Couleur de la carte
        self.couleur = ["Pique", "Trèfle", "Carreau", "Coeur"]
        #self.ComptA=0
        #self.ComptB=0


        for c in range(len(self.couleur)):
          for i in range(len(self.valeur)):
            self.carte.append((i, c))
      else :
        return 
  
    def nomCarteValeur(self, c):
        """Renvoie le nom de la carte (<c> doit être un tuple !!!)"""
        self.indice1, self.indice2 = c
        
        return self.valeur[self.indice1] 

          
    def nomCarteCouleur(self,c):
      self.indice1, self.indice2 = c
      return self.couleur[self.indice2]


      
    def remplissage(self):
      self.carte = []
      if self.compteur==1:
        self.carte =JeuCommun.carte[:26]
        return JeuCommun.carte[:26]
      else :
        self.carte =JeuCommun.carte[26:]
        return JeuCommun.carte[26:]


      
    def battre(self):
        """Mélange les cartes"""
        shuffle(self.carte)


    def tirer(self,nb):
        """Retire une carte du jeu"""
        select=self.carte[0]
        del(self.carte[0])
        return select
      
    def ajout(self,Jeusuivant):
      print()
      self.carte+=Jeusuivant

def ajoutcarteA (ja,jb,nb,ComptA,ComptB):
      JeuAsuivant.append(ja)
      JeuAsuivant.append(jb)
      for i in range(nb+1):
        ja=JeuA.tirer(0)
        jb=JeuB.tirer(0)
        JeuAsuivant.append(ja)
        JeuAsuivant.append(jb)
      return (ja,jb)
        
      
def ajoutcarteB (ja,jb,nb,ComptA,ComptB):
      JeuBsuivant.append(ja)
      JeuBsuivant.append(jb)
      for i in range(nb+1):
        ja=JeuA.tirer(0)
        jb=JeuB.tirer(0)
        JeuBsuivant.append(ja)
        JeuBsuivant.append(jb)
      return (ja,jb)




def égalité(ja,jb,nb,ComptA,ComptB,JeuAsuivant,JeuBsuivant):

      
      if len(JeuA.carte)<2 or len(JeuB.carte)<2 :
        print("impossible")
        JeuA.ajout(JeuAsuivant)
        JeuB.ajout(JeuBsuivant)
        print("on continue...")
      else:
        if JeuA.carte[nb]>JeuB.carte[nb]:
            ComptA+=nb+2
            ajoutcarteA(ja,jb,nb,ComptA,ComptB)
            print("   -> Joueur A gagne cette bataille")
            bataille (ja,jb,ComptA,ComptB)
        else:
            
              
          if JeuA.carte[nb]<JeuB.carte[nb] :
              ComptB+=nb+2
              ajoutcarteB(ja,jb,nb,ComptA,ComptB)
              print("   -> Joueur B gagne cette bataille")
              
              #print("Point de A :",int(ComptA))
              #print("Point de B :",int(ComptB))
              bataille (ja,jb,ComptA,ComptB)
          else:
            
               
            if JeuA.carte[nb]==JeuB.carte[nb] :
                égalité(ja,jb,nb+2,ComptA,ComptB,JeuAsuivant,JeuBsuivant)


def bataille (ja,jb,ComptA,ComptB):
      JeuAsuivant=[]
      JeuBsuivant=[]
  
      while len(JeuA.carte)>0  or len(JeuB.carte)>0 :
        
        if len(JeuB.carte)==0 or len(JeuA.carte)==0:
          newmelange(JeuA,JeuB,JeuAsuivant,JeuBsuivant)
          
        ja=JeuA.tirer(0)
        jb=JeuB.tirer(0)
        print("Joueur A =",JeuCommun.nomCarteValeur(ja),"de",JeuCommun.nomCarteCouleur(ja),"   Joueur B =", JeuCommun.nomCarteValeur(jb),"de",JeuCommun.nomCarteCouleur(jb), end='')







          
        if ja[0]>jb[0]:
          ComptA+=1
          JeuAsuivant.append(ja)
          JeuAsuivant.append(jb)
          #JeuA.ajoutcarte(ja,jb)
          print("   -> Joueur A gagne")

          
        if ja[0]<jb[0] :
          ComptB += 1
          JeuBsuivant.append(ja)
          JeuBsuivant.append(jb)
          #JeuB.ajoutcarte(ja,jb)
          print("   -> Joueur B gagne")

            
        if ja[0]==jb[0] :
          print("    -> Égalité")
          #print("Point de A :",int(ComptA))
          #print("Point de B :",int(ComptB))
          return égalité(ja,jb,1,ComptA,ComptB,JeuAsuivant,JeuBsuivant)
          



        print("Point de A :",int(ComptA))
        print("Point de B :",int(ComptB))
        #print()
        #print("jeu a suivant : ",JeuAsuivant)
        #print("jeu b suivant : ",JeuBsuivant)
        print()
        print(JeuA.carte)
        print(JeuB.carte)
      
            
      print()
      #print("Point de A :",int(ComptA))
      #print("Point de B :",int(ComptB))
      print()
      if ComptA>ComptB:
        print("Le A gagne avec ",int(ComptA),"points , Félicitation")
      if ComptA<ComptB:
        print("Le B gagne avec ",int(ComptB),"points , Félicitation")
      if ComptA==ComptB:
        print("Egalité entre A et B avec ",ComptA,"points")
      newmelange(JeuA,JeuB,JeuAsuivant,JeuBsuivant) 
      if len(JeuA.carte)==0 :
        print("Joueur B a gagné")
        print("Aurevoir")
      if len(JeuB.carte)==0 :
        print("Joueur A a gagné")
        print("Aurevoir")
        
          
        
def newmelange(JeuA,JeuB,JeuAsuivant,JeuBsuivant)  :
  time.sleep(2)
  print("On mélange")  
  #print(JeuAsuivant)
  JeuA.ajout(JeuAsuivant)
  JeuA.battre()        
  print("Jeu A :",JeuA.carte)
  #print(JeuBsuivant)
  JeuB.ajout(JeuBsuivant)
  JeuB.battre()
  print("Jeu B :",JeuB.carte)
  bataille(JeuA.carte,JeuB.carte,0,0)


JeuCommun= JeuDeCartes(0)
JeuCommun.battre()

JeuA = JeuDeCartes(1)
#print("JeuA :",JeuA.remplissage())
#JeuA.battre()
#print("Jeu A :",JeuA.carte)

JeuB= JeuDeCartes(2)
#print("JeuB :",JeuB.remplissage())
#JeuB.battre()
#print("Jeu B :",JeuB.carte)

ComptA = 0
ComptB = 0


JeuAsuivant=[]
JeuBsuivant=[]

ja=JeuA.remplissage()
jb=JeuB.remplissage()

bataille(ja,jb,ComptA,ComptB)