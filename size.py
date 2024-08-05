import os

def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
    return 0

def list_directory_by_size(directory_path):
    items = [(item, get_size(os.path.join(directory_path, item))) for item in os.listdir(directory_path)]
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    for item, size_bytes in sorted_items:
        size_mb = size_bytes / (1024 * 1024)  # Convert bytes to megabytes
        print(f"{item}: {size_mb:.2f} MB")

# Définissez le chemin du répertoire
directory_path = r'D:\\' 
# Liste les éléments du répertoire par taille décroissante en Mo
list_directory_by_size(directory_path)

r'C:\Users\HP\Documents\impactandpartners'