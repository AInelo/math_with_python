import pikepdf

def compress_pdf(input_pdf, output_pdf):
    with pikepdf.open(input_pdf) as pdf:
        # More aggressive compression settings
        pdf.save(output_pdf, 
                compress_streams=True,
                preserve_pdfa=False,
                object_stream_mode=pikepdf.ObjectStreamMode.generate,
                recompress_flate=True)

# Chemins des fichiers d'entrée et de sortie
input_pdf = "/home/ainelo23/Desktop/math_with_python/pdf/resizer/VF_Diplôme_et_Certificat_Travail_et_Formation_Toton.pdf"
output_pdf = "/home/ainelo23/Desktop/math_with_python/pdf/resizer/VF_Diplôme_et_Certificat_Travail_et_Formation_Toton_compressed.pdf"

# Appeler la fonction de compression
compress_pdf(input_pdf, output_pdf)

print(f"Le fichier a été compressé et sauvegardé sous {output_pdf}")
