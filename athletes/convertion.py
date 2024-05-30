import json

# Chemin vers le fichier JSON original
input_file_path = "athletes_final.json"

# Chemin vers le fichier SQL de sortie
output_file_path = "athletes_final.sql"

# Nom de la table et de la base de données
database_name = "projethackathon_projet2024"
table_name = "athlete"

# Lire et charger le contenu du fichier JSON
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Créer le fichier SQL
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(f"USE {database_name};\n\n")

    for entry in data:
        updates = []
        
        # Vérifier et ajouter la mise à jour pour event_title
        if "event_title" in entry and entry["event_title"]:
            event_title = entry["event_title"].replace("'", "''")
            updates.append(f"event_title = '{event_title}'")
        
        # Vérifier et ajouter la mise à jour pour discipline_title
        if "discipline_title" in entry and entry["discipline_title"]:
            discipline_title = entry["discipline_title"].replace("'", "''")
            updates.append(f"discipline_title = '{discipline_title}'")

        # Si des mises à jour sont présentes, générer la commande SQL
        if updates:
            athlete_url = entry["athlete_url"].replace("'", "''")
            updates_str = ", ".join(updates)
            file.write(f"UPDATE {table_name} SET {updates_str} WHERE athlete_url = '{athlete_url}';\n")

print(f"SQL script saved to {output_file_path}")
