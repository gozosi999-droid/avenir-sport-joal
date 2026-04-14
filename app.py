import streamlit as st
import base64
import os

# --- FONCTION POUR LE FOND ---
def set_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=2000");
             background-size: cover;
             background-attachment: fixed;
         }}
         /* Style pour rendre le texte lisible sur le fond */
         .main-title {{
             color: white;
             text-shadow: 2px 2px 8px #000000;
             text-align: center;
         }}
         .product-card {{
             background-color: rgba(255, 255, 255, 0.95);
             padding: 15px;
             border-radius: 10px;
             text-align: center;
             color: black;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# 1. Configuration de la page
st.set_page_config(page_title="Avenir Sport Joal", layout="wide")
set_bg_from_url()

# 2. AFFICHAGE UNIQUE DU LOGO ET DU NOM
col_logo, col_titre = st.columns([1, 4])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    else:
        st.write("⚽")

with col_titre:
    st.markdown("<h1 class='main-title'>🦁 AVENIR SPORT JOAL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; text-align: center;'>Le meilleur du sport à Joal-Fadiouth</p>", unsafe_allow_html=True)

st.write("---")

# 3. GRILLE DE PRODUITS (Comme sur ta photo)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/200x200.png?text=Maillot+Senegal")
    st.write("### Maillot Sénégal")
    st.write("Prix : 12 500 FCFA")
    st.link_button("🛍️ Commander", "https://wa.me/221XXXXXXXXX")
    st.markdown('</div>', unsafe_allow_html=True)

# Ajoute d'autres produits ici si tu veux...

