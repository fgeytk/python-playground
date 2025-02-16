import os
import shutil
from glob import glob

# Spécifie le dossier où tu veux copier les images
dossier_destination = r"C:\Users\CHARLES\Pictures"

# Extensions des fichiers images que tu veux récupérer
extensions_images = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.webp']


# Fonction pour récupérer toutes les images
def recuperer_images(source, destination):
    for ext in extensions_images:
        # Cherche les fichiers d'images dans tous les sous-dossiers
        fichiers = glob(os.path.join(source, '**', ext), recursive=True)

        for fichier in fichiers:
            try:
                # Copie chaque image dans le dossier de destination
                shutil.copy(fichier, destination)
                print(f"Image copiée: {fichier}")
            except Exception as e:
                print(f"Erreur lors de la copie de {fichier}: {e}")


# Récupère les images dans le répertoire utilisateur (ou spécifie le répertoire de départ)
dossier_source = r"C:\Users\CHARLES\Desktop"

# Appel de la fonction pour récupérer les images
recuperer_images(dossier_source, dossier_destination)
