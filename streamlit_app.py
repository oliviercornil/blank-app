import streamlit as st
import ezdxf
import pandas as pd

st.title('Extraction de données d’un fichier DXF')

# Télécharger un fichier DXF
uploaded_file = st.file_uploader("Téléchargez un fichier DXF", type="dxf")

if uploaded_file is not None:
    # Utilisez 'uploaded_file' comme fichier DXF
    doc = ezdxf.read(stream=uploaded_file)

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
