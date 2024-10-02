import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import ezdxf

# Charger le fichier DXF
file_path = "chemin/vers/votre_fichier.dxf"
doc = ezdxf.readfile(file_path)

# Parcourir toutes les entités dans le modèle et récupérer quelques informations
entities_info = []
for entity in doc.modelspace():
    entities_info.append({
        "type": entity.dxftype(),
        "layer": entity.dxf.layer
    })

# Convertir les informations en un DataFrame pour les afficher proprement
import pandas as pd
df_entities = pd.DataFrame(entities_info)

# Afficher les informations extraites
print(df_entities)
