import streamlit as st
import re

# Liste de données brutes que vous avez fournies
raw_data = [
    "{\\FArial;\\W4.24138; }Cuisine\\P{\\FArial;\\W0.83662; }H.S.P.: 245 cm \\P{\\FArial;\\W0.59852; }Niv.: + 000 cm",
    "{\\FArial;\\W3.74138; }Salle de {\\FArial;\\W3.74138; }restaurant\\P{\\FArial;\\W0.83662; }H.S.P.: 252 cm \\P{\\FArial;\\W0.59852; }Niv.: + 000 cm",
    "Salle évenementielle", "Salle de restaurant", "Cuisine",
    "{\\A1;\\H0.10000x;CUISINE}", "{\\A1;\\H0.10000x;CHAMBRE / BUREAU}", "{\\A1;\\H0.10000x;BUREAU - Espace professionnel }",
    # Ajoutez les autres entrées ici
]

# Liste des mots-clés que nous voulons extraire
keywords = ['cuisine', 'bureau', 'parking', 'restaurant', 'salle']

# Fonction pour nettoyer et extraire les mots-clés
def extract_room_names(data, keywords):
    cleaned_names = []
    
    for item in data:
        # Supprimer les balises inutiles avec une expression régulière
        cleaned_text = re.sub(r'{.*?}', '', item)
        cleaned_text = cleaned_text.strip()  # Supprimer les espaces superflus
        
        # Vérifier si un des mots-clés figure dans le texte nettoyé
        for keyword in keywords:
            if keyword in cleaned_text.lower():
                cleaned_names.append(cleaned_text)
                break  # On arrête la recherche dès qu'un mot-clé est trouvé

    return cleaned_names

# Titre de l'application Streamlit
st.title("Extraction des noms de pièces d'un fichier DXF")

# Afficher les données brutes pour information (facultatif)
st.write("Données brutes :")
st.write(raw_data)

# Extraire les noms des pièces
extracted_names = extract_room_names(raw_data, keywords)

# Afficher les noms extraits
st.write("Noms des pièces trouvés :")
st.write(extracted_names)

# Si aucune pièce n'est trouvée
if not extracted_names:
    st.write("Aucun nom de pièce trouvé.")

