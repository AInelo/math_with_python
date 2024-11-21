from PIL import Image
import os

def reduce_image_size(input_image_path, output_image_path, percent_reduction):
    # Ouvre l'image
    with Image.open(input_image_path) as img:
        # Calculer les nouvelles dimensions
        width, height = img.size
        new_width = int(width * (1 - percent_reduction / 100))
        new_height = int(height * (1 - percent_reduction / 100))
        
        # Redimensionne l'image
        resized_img = img.resize((new_width, new_height))
        
        # Enregistre l'image redimensionnée
        resized_img.save(output_image_path)
        
        # Affiche les informations sur la taille avant et après le redimensionnement
        original_size = os.path.getsize(input_image_path) / (1024 * 1024)  # Taille originale en Mo
        resized_size = os.path.getsize(output_image_path) / (1024 * 1024)  # Taille redimensionnée en Mo
        print(f"Image originale : {original_size:.2f} Mo")
        print(f"Image redimensionnée : {resized_size:.2f} Mo")

# Chemin de l'image d'entrée et de sortie
# input_image_path = 'chemin/vers/votre/image.jpg'
# input_image_path = r'C:\Users\HP\Documents\impactandpartners\Application_Web_Plan_Comptable_Impact_And_Partners\frontend\dashboard\static\profildashboard\non_lucratif.jpg'

input_image_path = r'C:\Users\HP\Pictures\math_with_python\image\resizer\logo-sw.png'

output_image_path = r'C:\Users\HP\Pictures\math_with_python\image\resizer\logo-sw-next.png'

# output_image_path = r'C:\Users\HP\Documents\impactandpartners\Application_Web_Plan_Comptable_Impact_And_Partners\frontend\dashboard\static\profildashboard\reduce\non_lucratif.jpg'

# Pourcentage de réduction de taille
percent_reduction = 70

# Appel de la fonction pour réduire la taille de l'image
reduce_image_size(input_image_path, output_image_path, percent_reduction)
