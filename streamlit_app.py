import streamlit as st
import ezdxf
import pandas as pd
from io import BytesIO

st.title('Extraction de données d’un fichier DXF')

# Télécharger un fichier DXF
uploaded_file = st.file_uploader("Téléchargez un fichier DXF", type="dxf")

if uploaded_file is not None:
    # Lire le fichier DXF en tant que bytes
    try:
        # ezdxf.readfile nécessite un fichier physique, donc on doit utiliser le mode binaire du fichier uploadé
        dxf_stream = BytesIO(uploaded_file.getvalue())  # Créer un flux de bytes depuis le fichier uploadé
        doc = ezdxf.read(dxf_stream)  # Charger le fichier depuis le flux en bytes

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


