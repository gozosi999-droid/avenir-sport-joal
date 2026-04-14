import streamlit as st
import base64
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Avenir Sport Joal", layout="wide")

# --- FONCTION POUR LE FOND SOMBRE ET STYLISÉ ---
def set_design():
    # Remplace l'URL ci-dessous par ton lien d'image si tu en as un, 
    # sinon celle-ci est une image de stade très pro.
    img_url = "https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=2000"
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

        /* Fond d'écran avec voile noir pour la lisibilité */
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                        url("{img_url}");
            background-size: cover;
            background-attachment: fixed;
        }}

        /* Titre Impact Sport */
        .titre-sport {{
            font-family: 'Bebas Neue', cursive;
            font-size: 100px !important;
            color: #ffda00; 
            text-align: center;
            text-transform: uppercase;
            font-style: italic;
            line-height: 1;
            text-shadow: 4px 4px 0px #000000;
            margin-bottom: 0px;
        }}

        .sous-titre {{
            color: white;
            text-align: center;
            letter-spacing: 5px;
            font-weight: bold;
            margin-top: -10px;
            margin-bottom: 30px;
        }}

        /* Cartes produits style Sport-Outlet */
        .product-card {{
            background-color: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: black;
            box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
        }}

        .price-tag {{
            background-color: #ffda00;
            color: black;
            font-weight: bold;
            font-size: 22px;
            padding: 5px 15px;
            border-radius: 5px;
            display: inline-block;
            margin: 10px 0;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_design()

# 2. LOGO ET TITRE
col_logo, col_titre = st.columns([1, 4])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
    else:
        st.write("⚽")

with col_titre:
    st.markdown('<p class="titre-sport">AVENIR SPORT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sous-titre">JOAL-FADIOUTH • SÉNÉGAL</p>', unsafe_allow_html=True)

st.write("---")

# 3. GRILLE DE PRODUITS
col1, col2, col3 = st.columns(3)

# Exemple Produit 1
with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x300.png?text=Maillot+Senegal", use_container_width=True)
    st.write("### MAILLOT SÉNÉGAL 2024")
    st.markdown('<div class="price-tag">12.500 FCFA</div>', unsafe_allow_html=True)
    st.link_button("🛍️ COMMANDER SUR WHATSAPP", "https://wa.me/221XXXXXXXXX?text=Je%20veux%20le%20maillot%20du%20Senegal")
    st.markdown('</div>', unsafe_allow_html=True)

# Exemple Produit 2
with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x300.png?text=Crampons+Nike", use_container_width=True)
    st.write("### CRAMPONS NIKE ELITE")
    st.markdown('<div class="price-tag">25.000 FCFA</div>', unsafe_allow_html=True)
    st.link_button("🛍️ COMMANDER SUR WHATSAPP", "https://wa.me/221XXXXXXXXX?text=Je%20veux%20les%20crampons%20Nike")
    st.markdown('</div>', unsafe_allow_html=True)

# Exemple Produit 3
with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x300.png?text=Ballon+Adidas", use_container_width=True)
    st.write("### BALLON ADIDAS LIGUE 1")
    st.markdown('<div class="price-tag">8.500 FCFA</div>', unsafe_allow_html=True)
    st.link_button("🛍️ COMMANDER SUR WHATSAPP", "https://wa.me/221XXXXXXXXX?text=Je%20veux%20le%20ballon%20Adidas")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align:center; color:white;'>© 2026 Avenir Sport Joal - Qualité & Performance</p>", unsafe_allow_html=True)
