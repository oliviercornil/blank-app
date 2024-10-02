import streamlit as st
import ezdxf
import pandas as pd
from io import BytesIO

st.title('Extraction de données d’un fichier DXF')

# Télécharger un fichier DXF
uploaded_file = st.file_uploader("Téléchargez un fichier DXF", type="dxf")

if uploaded_file is not None:
    # Lire le fichier DXF depuis le flux binaire
    uploaded_file_bytes = uploaded_file.read()  # Lire le fichier en bytes
    dxf_stream = BytesIO(uploaded_file_bytes)  # Créer un flux en mémoire

    # Charger le fichier DXF avec ezdxf depuis le flux
    try:
        doc = ezdxf.read(dxf_stream)  # Charger depuis le flux de bytes
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier DXF : {str(e)}")
    else:
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
else:
    st.warning("Veuillez télécharger un fichier DXF.")
