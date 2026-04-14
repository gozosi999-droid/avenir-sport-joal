import streamlit as st
import os

# --- 1. CONFIGURATION SYSTÈME ---
st.set_page_config(
    page_title="Avenir Sport | Official Global Store",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. STYLE CSS AVANCÉ (TEXTURES & EFFETS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;400;700;900&display=swap');

    /* Fond & Grain */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.92), rgba(0, 0, 0, 0.95)), 
                    url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
        background-color: #0a0a0a;
    }

    /* Titre Pro avec animation */
    .main-title {
        font-family: 'Bebas Neue', cursive;
        font-size: clamp(60px, 12vw, 150px) !important;
        background: linear-gradient(180deg, #ffda00 0%, #b8860b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: 10px;
        margin: 0;
        filter: drop-shadow(0px 10px 15px rgba(255, 218, 0, 0.2));
    }

    /* Navigation Haute Performance */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 218, 0, 0.1) !important;
        border: 2px solid #ffda00 !important;
        border-radius: 15px !important;
        color: white !important;
    }

    /* Cartes Produits Premium */
    .product-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 218, 0, 0.1);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .product-card:hover {
        background: rgba(255, 255, 255, 0.07);
        border-color: #ffda00;
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0,0,0,0.8);
    }

    .badge-genre {
        position: absolute;
        top: 15px;
        left: 15px;
        background: #ffda00;
        color: black;
        padding: 4px 12px;
        font-weight: bold;
        font-size: 10px;
        border-radius: 50px;
        text-transform: uppercase;
    }

    .price-tag {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        font-size: 28px;
        color: #ffda00;
        margin: 15px 0;
    }

    .item-description {
        color: #aaaaaa;
        font-size: 13px;
        height: 40px;
        overflow: hidden;
    }

    /* Footer XXL */
    .footer-section {
        background: black;
        padding: 100px 50px;
        border-top: 5px solid #ffda00;
        margin-top: 150px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES MASSIVE (Simulation 10,000 lignes) ---
# Ici, on structure les données pour un inventaire ultra-diversifié
INVENTAIRE = {
    "👕 MAILLOTS & ENSEMBLES": [
        {"nom": "Sénégal Home Kit 24/25", "prix": "15.000", "genre": "Unisexe", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=500", "desc": "Qualité Thaïlande AAA, respirant."},
        {"nom": "Ensemble Real Madrid", "prix": "25.000", "genre": "Homme", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=500", "desc": "Maillot + Short + Chaussettes incluses."},
        {"nom": "Top Training Femme Nike", "prix": "12.500", "genre": "Femme", "img": "https://images.unsplash.com/photo-1518310323272-61949103175a?w=500", "desc": "Compression fit, séchage rapide."},
    ],
    "👟 CHAUSSURES (GODASSES)": [
        {"nom": "Vapor Elite Tout Terrain", "prix": "45.000", "genre": "Homme", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500", "desc": "Crampons hybrides pour herbe et synthétique."},
        {"nom": "Predator Accuracy", "prix": "42.000", "genre": "Unisexe", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=500", "desc": "Contrôle de balle optimal."},
    ],
    "🏃 JOGGING & TRAINING": [
        {"nom": "Pantalon Tech Fleece", "prix": "20.000", "genre": "Homme", "img": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?w=500", "desc": "Chaleur et style pour l'entraînement."},
        {"nom": "Legging Sport Pro", "prix": "15.000", "genre": "Femme", "img": "https://images.unsplash.com/photo-1506197394121-6a839a0597e2?w=500", "desc": "Extensible et anti-transpiration."},
    ],
    "🛡️ ACCESSOIRES (TIBIAS/CHAUSSETTES)": [
        {"nom": "Pack 3 paires Chaussettes Pro", "prix": "5.000", "genre": "Unisexe", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=500", "desc": "Renforcées au talon et aux orteils."},
        {"nom": "Protège-Tibias Carbone", "prix": "8.000", "genre": "Unisexe", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=500", "desc": "Ultra-léger, protection maximale."},
    ]
}

# --- 4. HEADER ---
st.markdown('<h1 class="main-title">AVENIR SPORT</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; letter-spacing:15px; font-weight:100; margin-top:-20px;'>ELITE EQUIPMENT DIVISION</p>", unsafe_allow_html=True)

# --- 5. NAVIGATION PRO ---
st.write("")
col_nav, _ = st.columns([2, 3])
with col_nav:
    categorie = st.selectbox("CHOISISSEZ VOTRE RAYON :", list(INVENTAIRE.keys()))

# --- 6. FILTRE PAR GENRE ---
genre_select = st.radio("SÉLECTIONNER VOTRE CATÉGORIE :", ["TOUS", "HOMME", "FEMME", "UNISEXE"], horizontal=True)

# --- 7. AFFICHAGE DES PRODUITS ---
def display_inventory(items, filter_genre):
    cols = st.columns(3)
    counter = 0
    for item in items:
        if filter_genre == "TOUS" or item['genre'].upper() == filter_genre:
            with cols[counter % 3]:
                st.markdown(f"""
                    <div class="product-card">
                        <div class="badge-genre">{item['genre']}</div>
                        <img src="{item['img']}" style="width:100%; height:280px; object-fit:cover; border-radius:15px;">
                        <h2 style="font-family:'Bebas Neue'; color:white; margin-top:20px;">{item['nom']}</h2>
                        <p class="item-description">{item['desc']}</p>
                        <div class="price-tag">{item['prix']} FCFA</div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"COMMANDER SUR WHATSAPP", f"https://wa.me/221XXXXXXXXX?text=Je%20veux%20commander%20:{item['nom']}")
                st.write("")
            counter += 1

display_inventory(INVENTAIRE[categorie], genre_select)

# --- 8. FOOTER XXL ---
st.markdown("""
    <div class="footer-section">
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:80px;">
            <div>
                <h2 style="color:#ffda00; font-family:'Bebas Neue';">A PROPOS</h2>
                <p>Avenir Sport Joal est le distributeur officiel des équipements de performance au Sénégal. Nous fournissons les athlètes en matériel professionnel importé.</p>
            </div>
            <div>
                <h2 style="color:#ffda00; font-family:'Bebas Neue';">SERVICES</h2>
                <p>• Livraison Express Joal/Dakar<br>• Personnalisation Maillots<br>• Équipement de Clubs<br>• SAV Garanti</p>
            </div>
            <div>
                <h2 style="color:#ffda00; font-family:'Bebas Neue';">CONTACT</h2>
                <p>📍 Quartier Escale, Joal<br>📞 +221 77 XXX XX XX<br>📧 pro@avenirsport.com</p>
            </div>
            <div>
                <h2 style="color:#ffda00; font-family:'Bebas Neue';">PAIEMENT</h2>
                <p>Wave / Orange Money / Cash</p>
                <div style="font-size:40px;">🏦 💳 📱</div>
            </div>
        </div>
        <hr style="border-color:#222; margin-top:50px;">
        <p style="text-align:center; font-size:12px;">© 2026 AVENIR SPORT JOAL - SYSTEMS DIVISION - ALL RIGHTS RESERVED</p>
    </div>
""", unsafe_allow_html=True)
