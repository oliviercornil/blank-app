import streamlit as st
import ezdxf
import pandas as pd
from io import BytesIO
import tempfile

st.title('Extraction des noms de pièces d’un fichier DXF')

# Télécharger un fichier DXF
uploaded_file = st.file_uploader("Téléchargez un fichier DXF", type="dxf")

if uploaded_file is not None:
    try:
        # Créer un fichier temporaire pour y écrire le contenu du fichier DXF
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())  # Écrire le contenu dans le fichier temporaire
            tmp_file_path = tmp_file.name

        # Lire le fichier DXF à partir du fichier temporaire
        doc = ezdxf.readfile(tmp_file_path)

        # Extraire des entités de texte (TEXT et MTEXT)
        room_names = []
        for entity in doc.modelspace():
            if entity.dxftype() == 'TEXT' or entity.dxftype() == 'MTEXT':
                text_content = entity.dxf.text
                # Filtrer les textes par exemple pour "chambre", "salon", etc.
                if any(keyword in text_content.lower() for keyword in ['chambre', 'salon', 'cuisine', 'salle', 'bureau']):
                    room_names.append(text_content)

        # Afficher les noms de pièces
        if room_names:
            st.write("Noms des pièces trouvés :")
            st.write(room_names)
        else:
            st.write("Aucun nom de pièce trouvé.")

    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier DXF : {str(e)}")
else:
    st.warning("Veuillez télécharger un fichier DXF.")
