import streamlit as st
import ezdxf
import pandas as pd
import tempfile
from io import BytesIO
import re

# Fonction pour extraire les entités texte d'un fichier DXF
def extract_text_entities(doc, keywords):
    room_names = []
    
    # Parcourir les entités dans le modèle DXF
    for entity in doc.modelspace():
        if entity.dxftype() in ['TEXT', 'MTEXT']:  # Filtrer les entités texte
            text_content = entity.dxf.text if entity.dxftype() == 'TEXT' else entity.text
            
            # Nettoyer le texte (enlever les balises potentielles)
            cleaned_text = re.sub(r'{.*?}', '', text_content).strip()
            
            # Filtrer selon les mots-clés (com
