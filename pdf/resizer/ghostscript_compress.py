import subprocess

def compress_pdf(input_path, output_path):
    gs_command = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/screen',
        '-dColorImageDownsampleType=/Bicubic',
        '-dColorImageResolution=72',
        '-dGrayImageDownsampleType=/Bicubic',
        '-dGrayImageResolution=72',
        '-dMonoImageDownsampleType=/Bicubic',
        '-dMonoImageResolution=72',
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_path}',
        input_path
    ]

    try:
        subprocess.run(gs_command, check=True)
        print(f"Compression terminée. Fichier sauvegardé: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la compression: {e}")

# Chemins des fichiers
input_pdf = "/home/ainelo23/Desktop/math_with_python/pdf/resizer/VF_Diplôme_et_Certificat_Travail_et_Formation_Toton.pdf"
output_pdf = "/home/ainelo23/Desktop/math_with_python/pdf/resizer/VF_Diplôme_et_Certificat_Travail_et_Formation_Toton_compressed.pdf"

compress_pdf(input_pdf, output_pdf) 