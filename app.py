import streamlit as st
import os

# --- 1. CONFIGURATION SYSTÈME ---
st.set_page_config(
    page_title="AVENIR SPORT | Elite Performance Store",
    page_icon="👑",
    layout="wide"
)

# --- 2. ARCHITECTURE CSS COMPLEXE (DARK & GOLD PREMIUM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@100;400;900&display=swap');

    /* Fond d'écran avec texture Carbone et dégradé */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #000000 100%);
        color: white;
    }

    /* Titre Monumental avec Animation Néon Or */
    .main-title {
        font-family: 'Bebas Neue';
        font-size: clamp(80px, 15vw, 180px) !important;
        text-align: center;
        background: linear-gradient(to bottom, #ffda00, #8a6d3b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        filter: drop-shadow(0 0 20px rgba(255, 218, 0, 0.4));
        animation: glow 2s ease-in-out infinite alternate;
    }

    /* Rayons "Tracés" avec bordures biseautées */
    .section-header {
        font-family: 'Bebas Neue';
        font-size: 50px;
        color: #ffda00;
        border-bottom: 3px solid #ffda00;
        padding-bottom: 10px;
        margin-bottom: 40px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    /* Cartes Produits : Glassmorphism Haute Qualité */
    .product-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
    }

    .product-card:hover {
        background: rgba(255, 218, 0, 0.1);
        border-color: #ffda00;
        transform: translateY(-20px) scale(1.05);
        box-shadow: 0 30px 60px rgba(0,0,0,0.9);
    }

    .product-card img {
        width: 100%;
        height: 300px;
        object-fit: cover;
        border-radius: 20px;
        margin-bottom: 20px;
    }

    /* Badge Catégorie (Homme, Femme, Unisexe) */
    .category-badge {
        position: absolute;
        top: 20px;
        right: 20px;
        background: #ffda00;
        color: black;
        padding: 5px 15px;
        font-weight: 900;
        font-size: 12px;
        border-radius: 50px;
        text-transform: uppercase;
    }

    .price-tag {
        font-family: 'Montserrat';
        font-size: 32px;
        font-weight: 900;
        color: #ffda00;
        margin: 15px 0;
    }

    /* Footer XXL Professionnel */
    .footer-xxl {
        background: #000;
        padding: 100px 50px;
        margin-top: 150px;
        border-top: 5px solid #ffda00;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES INVENTAIRE (Structure Massive) ---
STOCK = {
    "MAILLOTS & TRAINING": [
        {"nom": "Sénégal Home Kit 24/25", "prix": "15.000", "cat": "Unisexe", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=600"},
        {"nom": "Ensemble Jogging Nike Tech", "prix": "45.000", "cat": "Homme", "img": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?w=600"},
        {"nom": "Maillot Real Madrid Elite", "prix": "18.500", "cat": "Homme", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=600"},
        {"nom": "Brassière Training Pro", "prix": "12.000", "cat": "Femme", "img": "https://images.unsplash.com/photo-1518310323272-61949103175a?w=600"},
    ],
    "CHAUSSURES & GODASSES": [
        {"nom": "Mercurial Vapor 15 Elite", "prix": "45.000", "cat": "Unisexe", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600"},
        {"nom": "Predator Accuracy +", "prix": "42.500", "cat": "Homme", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=600"},
        {"nom": "Basket Running Femme Cloud", "prix": "35.000", "cat": "Femme", "img": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600"},
    ],
    "ACCESSOIRES & PROTECTION": [
        {"nom": "Protège-tibias Carbone", "prix": "8.500", "cat": "Unisexe", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=600"},
        {"nom": "Chaussettes de Match Pro", "prix": "3.500", "cat": "Unisexe", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=600"},
    ]
}

# --- 4. HEADER ---
st.markdown('<h1 class="main-title">AVENIR SPORT</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; letter-spacing:20px; font-weight:100; opacity:0.6;'>DIVISION JOAL-FADIOUTH</p>", unsafe_allow_html=True)

# --- 5. NAVIGATION & FILTRAGE ---
st.write("---")
nav_col1, nav_col2 = st.columns([2, 1])
with nav_col1:
    rayon = st.radio("SÉLECTIONNEZ VOTRE RAYON :", list(STOCK.keys()), horizontal=True)
with nav_col2:
    filtre = st.selectbox("FILTRER PAR GENRE :", ["TOUT", "HOMME", "FEMME", "UNISEXE"])

# --- 6. MOTEUR D'AFFICHAGE ---
def generate_catalog(data, filter_cat):
    cols = st.columns(3)
    idx = 0
    for item in data:
        if filter_cat == "TOUT" or item['cat'].upper() == filter_cat:
            with cols[idx % 3]:
                st.markdown(f"""
                    <div class="product-card">
                        <div class="category-badge">{item['cat']}</div>
                        <img src="{item['img']}">
                        <h2 style="font-family:'Bebas Neue'; letter-spacing:2px; margin:0;">{item['nom']}</h2>
                        <div class="price-tag">{item['prix']} F</div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"COMMANDER SUR WHATSAPP", f"https://wa.me/221XXXXXXXXX?text=Bonjour%20Avenir%20Sport,%20je%20veux%20commander%20:{item['nom']}")
                st.write("")
                idx += 1

st.markdown(f'<div class="section-header">{rayon}</div>', unsafe_allow_html=True)
generate_catalog(STOCK[rayon], filtre)

# --- 7. FOOTER XXL (CORRIGÉ & TRÈS LONG) ---
st.markdown("""
    <div class="footer-xxl">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 50px; color: #888;">
            <div>
                <h2 style="color:#ffda00; font-family:'Bebas Neue';">L'EMPIRE AVENIR SPORT</h2>
                <p>Depuis Joal, nous équipons les futurs champions du Sénégal avec les meilleures marques mondiales. Qualité Thaïlande Import et équipements pro.</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">HORAIRES D'OUVERTURE</h4>
                <p>Lundi - Samedi : 09:00 - 22:00<br>Dimanche : 10:00 - 18:00</p>
                <h4 style="color:#ffda00; margin-top:20px;">LIVRAISON</h4>
                <p>Joal-Fadiouth : Instantanée<br>Dakar / Mbour : 24H</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">SERVICE CLIENT</h4>
                <p>📞 +221 77 XXX XX XX</p>
                <p>📧 contact@avenirsportjoal.com</p>
                <p>💬 WhatsApp Business Actif</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">SUIVEZ-NOUS</h4>
                <p>📸 Instagram: @avenirsport_joal</p>
                <p>👤 Facebook: Avenir Sport Sénégal</p>
                <p>🎵 TikTok: @avenirsport_empire</p>
            </div>
        </div>
        <hr style="border-color: #222; margin: 60px 0;">
        <p style="text-align: center; font-size: 10px; letter-spacing: 2px;">© 2026 AVENIR SPORT JOAL - TOUS DROITS RÉSERVÉS - SITE OFFICIEL</p>
    </div>
""", unsafe_allow_html=True)
