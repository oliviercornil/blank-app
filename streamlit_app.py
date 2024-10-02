import streamlit as st
import ezdxf
import pandas as pd
from io import BytesIO
import tempfile

st.title('Extraction de données d’un fichier DXF')

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

        # Extraire des informations des entités
        entities_info = []
        for entity in doc.modelspace():
            entities_info.append({
                "type": entity.dxftype(),
                "layer": entity.dxf.layer
            })

        # Afficher les informations dans un tableau
        df_entities = pd.DataFrame(entities_info)
        st.write(df_entities)

    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier DXF : {str(e)}")
else:
    st.warning("Veuillez télécharger un fichier DXF.")
