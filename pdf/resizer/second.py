from PyPDF2 import PdfReader, PdfWriter
import io

def compress_pdf(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Copier chaque page avec compression
    for page in reader.pages:
        writer.add_page(page)
    
    # Appliquer la compression lors de l'écriture
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# Chemins des fichiers d'entrée et de sortie
input_pdf = "/home/ainelo23/Desktop/math_with_python/pdf/resizer/VF_Diplôme_et_Certificat_Travail_et_Formation_Toton.pdf"
output_pdf = "/home/ainelo23/Desktop/math_with_python/pdf/resizer/VF_Diplôme_et_Certificat_Travail_et_Formation_Toton_compressed.pdf"

# Appeler la fonction de compression
compress_pdf(input_pdf, output_pdf)

print(f"Le fichier a été compressé et sauvegardé sous {output_pdf}")
