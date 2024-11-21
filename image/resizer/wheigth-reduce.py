from PIL import Image
import os

def reduce_image_size_under_limit(input_image_path, output_image_path, max_size_mb):
    # Ouvre l'image
    with Image.open(input_image_path) as img:
        # Qualité initiale
        quality = 95
        # Enregistre avec la qualité initiale
        img.save(output_image_path, quality=quality)
        
        # Réduit la qualité jusqu'à ce que la taille soit sous la limite
        while os.path.getsize(output_image_path) > (max_size_mb * 1024 * 1024) and quality > 5:
            quality -= 5
            img.save(output_image_path, quality=quality)
        
        # Affiche les informations sur la taille
        original_size = os.path.getsize(input_image_path) / (1024 * 1024)
        final_size = os.path.getsize(output_image_path) / (1024 * 1024)
        print(f"Taille originale : {original_size:.2f} Mo")
        print(f"Taille finale : {final_size:.2f} Mo")
        print(f"Qualité finale : {quality}")

# Exemple d'utilisation
input_path = "chemin/vers/image_originale.jpg"
output_path = "chemin/vers/image_reduite.jpg" 
max_size = 1.0  # Taille maximale en Mo

reduce_image_size_under_limit(input_path, output_path, max_size)

