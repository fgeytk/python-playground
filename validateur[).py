def ouvrant(file,symbole):
     return (file.appends(symbole))

def défiler(file):
 file.pop()

def associes(file,element):
  ouvrant=['(','[','{','<']
  fermant=[')',']','}','>']
  if element==ouvrant :
    return True
  if element==fermant :
    return True


def validateur(LS):
  pile=[]
  Ok=  True
  indice=0
  while Ok and indice < len(pile):
    symbole =LS[indice]
    indice= indice+1
    ouvrant(symbole)
    if len(pile)==0: 
       Ok=False
    else:
        défiler(pile)
        Ok = associes(pile,symbole)
  if len(pile)>0:
   Ok=False
  return Ok

LS1 = ['(','[','(',']']
print(validateur(LS1))