import streamlit as st
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Avenir Sport Joal | Boutique Elite", layout="wide")

# --- DESIGN CSS ULTRA-COMPLEXE (Navigation & Textures) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;500;700&display=swap');

    /* Fond d'écran avec texture grainée et overlay sombre */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.8)), 
                    url("https://images.unsplash.com/photo-1534158914592-062992fbe900?q=80&w=2000");
        background-size: cover;
        background-attachment: fixed;
    }

    /* TITRE IMPACT AVEC EFFET MÉTALLIQUE */
    .titre-sport {
        font-family: 'Bebas Neue';
        font-size: 110px !important;
        background: linear-gradient(180deg, #ffda00 0%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        text-transform: uppercase;
        font-style: italic;
        margin-bottom: 0px;
        filter: drop-shadow(4px 4px 2px #000);
    }

    /* MODIFICATION DE LA BARRE DE NAVIGATION (TABS) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: rgba(255, 218, 0, 0.1); /* Texture Verre Jaune */
        border-radius: 10px 10px 0px 0px;
        color: white !important;
        font-family: 'Bebas Neue';
        font-size: 22px;
        padding: 0px 30px;
        border: 1px solid rgba(255, 218, 0, 0.3);
        transition: 0.3s;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffda00 !important;
        color: black !important;
        border: 1px solid #ffda00;
        transform: translateY(-5px);
    }

    /* BANNIÈRES DE RAYONS TRACÉES */
    .rayon-header {
        border-left: 15px solid #ffda00;
        background: rgba(255,255,255,0.05);
        padding: 15px 25px;
        color: white;
        font-family: 'Bebas Neue';
        font-size: 45px;
        margin: 40px 0px;
        letter-spacing: 2px;
    }

    /* CARTES PRODUITS PRO */
    .product-card {
        background: rgba(255, 255, 255, 0.98);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.8);
        transition: 0.4s;
    }
    .product-card:hover {
        transform: rotate(1deg) scale(1.02);
    }

    .price-tag {
        background-color: #000;
        color: #ffda00;
        font-weight: 900;
        font-size: 24px;
        padding: 5px 20px;
        border-radius: 8px;
        display: inline-block;
        margin: 15px 0;
    }

    /* FOOTER XXL */
    .footer-xxl {
        background: #000;
        color: white;
        padding: 80px 50px;
        border-top: 10px solid #ffda00;
        margin-top: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DONNÉES ÉTENDUE (CODE PLUS LONG)
CATALOGUE = {
    "MAILLOTS": [
        {"nom": "Sénégal Home 24/25", "prix": "15.000", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?q=80&w=600"},
        {"nom": "Real Madrid Home", "prix": "18.500", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?q=80&w=600"},
        {"nom": "Manchester City", "prix": "17.000", "img": "https://images.unsplash.com/photo-1589487391730-58f20eb2c308?q=80&w=600"},
        {"nom": "FC Barcelone Home", "prix": "18.500", "img": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?q=80&w=600"},
        {"nom": "PSG Jordan Edition", "prix": "18.000", "img": "https://images.unsplash.com/photo-1614632537190-23e444104533?q=80&w=600"},
        {"nom": "Arsenal Red Cannon", "prix": "17.000", "img": "https://images.unsplash.com/photo-1521731902048-96593a12a322?q=80&w=600"},
    ],
    "CHAUSSURES": [
        {"nom": "Nike Mercurial Pro", "prix": "35.000", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=600"},
        {"nom": "Adidas Predator 24", "prix": "33.000", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?q=80&w=600"},
        {"nom": "Puma Future Ultimate", "prix": "30.000", "img": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?q=80&w=600"},
        {"nom": "Nike Phantom GX", "prix": "38.000", "img": "https://images.unsplash.com/photo-1511556532299-8f662fc26c06?q=80&w=600"},
    ]
}

# 3. INTERFACE PRINCIPALE
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=200)
with col2:
    st.markdown('<h1 class="titre-sport">AVENIR SPORT</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ffda00; letter-spacing:12px; font-size:20px;'>ELITE PERFORMANCE JOAL</p>", unsafe_allow_html=True)

# NAVIGATION PAR ONGLETS (STYLE MODIFIÉ)
tab_home, tab_maillots, tab_shoes, tab_contact = st.tabs([
    "🏠 ACCUEIL", "👕 MAILLOTS", "👟 CHAUSSURES", "📞 CONTACT"
])

# FONCTION D'AFFICHAGE PRO
def generer_grille(produits):
    cols = st.columns(3)
    for index, item in enumerate(produits):
        with cols[index % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" style="width:100%; height:250px; object-fit:cover; border-radius:10px;">
                    <h2 style="font-family:'Bebas Neue'; letter-spacing:1px; margin-top:15px;">{item['nom']}</h2>
                    <div class="price-tag">{item['prix']} FCFA</div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"COMMANDER {item['nom']}", f"https://wa.me/221XXXXXXXXX")
            st.write("---")

# --- CONTENU DES ONGLETS ---
with tab_home:
    st.markdown('<div class="rayon-header">★ ARRIVAGES EXCLUSIFS</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1543326727-cf6c39e8f84c?q=80&w=2000", caption="Nouveaux Ballons et Equipements")
    st.write("### Bienvenue dans la référence sport de Joal-Fadiouth")
    st.info("Découvrez notre sélection de maillots Qualité Thaïlande et Chaussures Pro.")

with tab_maillots:
    st.markdown('<div class="rayon-header">RAYON MAILLOTS OFFICIELS</div>', unsafe_allow_html=True)
    generer_grille(CATALOGUE["MAILLOTS"])

with tab_shoes:
    st.markdown('<div class="rayon-header">RAYON CRAMPONS & RUNNING</div>', unsafe_allow_html=True)
    generer_grille(CATALOGUE["CHAUSSURES"])

with tab_contact:
    st.markdown('<div class="rayon-header">CONTACTEZ LA BOUTIQUE</div>', unsafe_allow_html=True)
    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
        <div style="background:rgba(255,255,255,0.1); padding:40px; border-radius:20px; color:white;">
            <h2 style="color:#ffda00;">📍 ADRESSE</h2>
            <p style="font-size:20px;">Joal-Fadiouth, Quartier Escale<br>Sénégal</p>
            <h2 style="color:#ffda00;">📞 TÉLÉPHONE</h2>
            <p style="font-size:20px;">+221 77 XXX XX XX<br>+221 70 XXX XX XX</p>
        </div>
        """, unsafe_allow_html=True)

# 4. FOOTER XXL (TRÈS LONG)
st.markdown("""
    <div class="footer-xxl">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px;">
            <div>
                <h2 style="color:#ffda00; font-family:'Bebas Neue';">AVENIR SPORT JOAL</h2>
                <p>La destination n°1 pour les passionnés de foot.<br>Qualité supérieure garantie.</p>
