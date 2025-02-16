import os
import shutil
from glob import glob

dossier_destination = r"C:\Users\CHARLES\Pictures"
extensions_images = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.webp']

def recuperer_images(source, destination):
    for ext in extensions_images:
        fichiers = glob(os.path.join(source, '**', ext), recursive=True)

        for fichier in fichiers:
            try:
                shutil.copy(fichier, destination)
                print(f"Image copiée: {fichier}")
            except Exception as e:
                print(f"Erreur lors de la copie de {fichier}: {e}")

dossier_source = r"C:\Users\CHARLES\Desktop"
recuperer_images(dossier_source, dossier_destination)
