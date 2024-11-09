import pikepdf

def compress_pdf(input_pdf, output_pdf):
    with pikepdf.open(input_pdf) as pdf:
        # Optimiser le fichier PDF
        pdf.save(output_pdf, compress_streams=True)

# Chemins des fichiers d'entrée et de sortie
input_pdf = r"C:\Users\HP\Pictures\math_with_python\pdf\resizer\VF_Diplôme_et_Certificat_Travail_et_Formation_Toton.pdf"
output_pdf = r"C:\Users\HP\Pictures\math_with_python\pdf\resizer\VF_Diplôme_et_Certificat_Travail_et_Formation_Toton_compressed.pdf"

# Appeler la fonction de compression
compress_pdf(input_pdf, output_pdf)

print(f"Le fichier a été compressé et sauvegardé sous {output_pdf}")
