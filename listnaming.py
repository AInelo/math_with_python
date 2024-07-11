import os

def generate_import_statements(directory_path):
    import_statements = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.css'):  # Filtrer les fichiers CSS
                relative_path = os.path.relpath(os.path.join(root, file), directory_path)
                import_statement = f"import '../css/navbar/element/{relative_path.replace(os.sep, '/')}';"
                import_statements.append(import_statement)
    
    for statement in import_statements:
        print(statement)

# Exemple d'utilisation

directory_path = r"C:\Users\HP\Music\positiv-project\src\css\navbar\element"
generate_import_statements(directory_path)
