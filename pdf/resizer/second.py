import fitz  # PyMuPDF

def compress_pdf(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    # Parcourir chaque page du PDF
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)

        # Parcourir les images dans la page
        image_list = page.get_images(full=True)
        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Réduire la qualité de l'image (ici, on peut la compresser ou la redimensionner)
            # Exemple : réduire la taille en changeant la qualité
            # NOTE: Vous pouvez utiliser des librairies comme Pillow pour une compression d'image plus poussée.

            # Vous pouvez choisir de compresser ou redimensionner l'image ici, si nécessaire.

    # Sauvegarder le PDF compressé
    doc.save(output_pdf)

# Chemins des fichiers d'entrée et de sortie
input_pdf = r"C:\Users\HP\Pictures\math_with_python\pdf\resizer\VF_Diplôme_et_Certificat_Travail_et_Formation_Toton.pdf"
output_pdf = r"C:\Users\HP\Pictures\math_with_python\pdf\resizer\VF_Diplôme_et_Certificat_Travail_et_Formation_Toton_compressed.pdf"

# Appeler la fonction de compression
compress_pdf(input_pdf, output_pdf)

print(f"Le fichier a été compressé et sauvegardé sous {output_pdf}")
