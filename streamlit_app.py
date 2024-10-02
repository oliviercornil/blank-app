import ezdxf
import pandas as pd

# Chemin vers votre fichier DXF
file_path = "chemin/vers/votre_fichier.dxf"

# Lire le fichier DXF
doc = ezdxf.readfile(file_path)

# Extraire des entités de texte (TEXT et MTEXT)
room_names = []
for entity in doc.modelspace():
    if entity.dxftype() == 'TEXT' or entity.dxftype() == 'MTEXT':
        text_content = entity.dxf.text
        # Filtrer les textes pour "chambre", "salon", etc.
        if any(keyword in text_content.lower() for keyword in ['chambre', 'salon', 'cuisine', 'salle', 'bureau']):
            room_names.append(text_content)

# Afficher les noms des pièces trouvés
print("Noms des pièces trouvés :", room_names)
