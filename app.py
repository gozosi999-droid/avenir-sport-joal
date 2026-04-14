import streamlit as st
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Avenir Sport Joal | Boutique Officielle", layout="wide", page_icon="⚽")

# --- DESIGN CSS ULTRA-PROFESSIONNEL (STYLE CITY SPORT / NIKE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;400;700&display=swap');

    /* Fond d'écran avec Overlay Sombre */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url("https://images.unsplash.com/photo-1551952237-954a0e68786c?q=80&w=2000");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Titre Géant Impact */
    .titre-sport {
        font-family: 'Bebas Neue', cursive;
        font-size: clamp(60px, 10vw, 120px) !important;
        color: #ffda00; 
        text-align: center;
        text-transform: uppercase;
        font-style: italic;
        line-height: 0.8;
        text-shadow: 6px 6px 0px #000000;
        margin-bottom: 0px;
    }

    /* Rayons Tracés */
    .rayon-banner {
        background: linear-gradient(90deg, #ffda00 0%, #000000 100%);
        color: black;
        font-family: 'Bebas Neue';
        font-size: 35px;
        padding: 10px 30px;
        border-radius: 0 50px 50px 0;
        margin: 40px 0 20px 0;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
    }

    /* Carte Produit Luxe */
    .product-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a !important;
        box-shadow: 0px 20px 40px rgba(0,0,0,0.6);
        transition: 0.4s ease;
        border: 1px solid #eee;
    }
    .product-card:hover {
        transform: scale(1.03);
        border: 2px solid #ffda00;
    }

    .price-tag {
        background-color: #ffda00;
        color: black;
        font-weight: 900;
        font-size: 26px;
        padding: 8px 25px;
        border-radius: 10px;
        display: inline-block;
        margin: 15px 0;
        font-family: 'Bebas Neue';
    }

    /* Footer Noir XXL */
    .footer-xxl {
        background-color: #000000;
        color: white;
        padding: 80px 40px;
        margin-top: 100px;
        border-top: 8px solid #ffda00;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DONNÉES DU MAGASIN (C'est ici que tu peux ajouter des centaines de lignes)
MAILLOTS = [
    {"nom": "Maillot Sénégal Home 2024", "prix": "15.000", "img": "https://via.placeholder.com/400x400.png?text=Senegal+Home"},
    {"nom": "Maillot Real Madrid 2025", "prix": "17.500", "img": "https://via.placeholder.com/400x400.png?text=Real+Madrid"},
    {"nom": "Maillot Barça Home", "prix": "17.500", "img": "https://via.placeholder.com/400x400.png?text=Barca"},
    {"nom": "Maillot Sénégal Away", "prix": "15.000", "img": "https://via.placeholder.com/400x400.png?text=Senegal+Away"},
    {"nom": "Maillot Manchester City", "prix": "17.000", "img": "https://via.placeholder.com/400x400.png?text=Man+City"},
    {"nom": "Maillot PSG 2025", "prix": "17.000", "img": "https://via.placeholder.com/400x400.png?text=PSG"},
]

CHAUSSURES = [
    {"nom": "Nike Mercurial Vapor", "prix": "35.000", "img": "https://via.placeholder.com/400x400.png?text=Nike+Vapor"},
    {"nom": "Adidas Predator", "prix": "32.500", "img": "https://via.placeholder.com/400x400.png?text=Adidas+Predator"},
    {"nom": "Puma Future7", "prix": "30.000", "img": "https://via.placeholder.com/400x400.png?text=Puma+Future"},
    {"nom": "Nike Phantom GX", "prix": "38.000", "img": "https://via.placeholder.com/400x400.png?text=Nike+Phantom"},
]

HABITS = [
    {"nom": "Survêtement Tech Fleece", "prix": "45.000", "img": "https://via.placeholder.com/400x400.png?text=Tech+Fleece"},
    {"nom": "Ensemble Training Sénégal", "prix": "25.000", "img": "https://via.placeholder.com/400x400.png?text=Training+SN"},
    {"nom": "Short Sport Nike", "prix": "8.500", "img": "https://via.placeholder.com/400x400.png?text=Short+Nike"},
]

# 3. EN-TÊTE DU SITE
col_l, col_r = st.columns([1, 4])
with col_l:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=200)
with col_r:
    st.markdown('<p class="titre-sport">AVENIR SPORT</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white; letter-spacing:10px; font-weight:bold; opacity:0.8;'>L'ÉLITE DU SPORT À JOAL-FADIOUTH</p>", unsafe_allow_html=True)

st.write("---")

# 4. NAVIGATION PAR ONGLETS (TABS)
tab_home, tab_maillots, tab_shoes, tab_habits, tab_contact = st.tabs([
    "🏠 ACCUEIL", "👕 MAILLOTS", "👟 CHAUSSURES", "🧥 HABITS", "📞 CONTACT"
])

# --- FONCTION POUR AFFICHER LES PRODUITS ---
def afficher_catalogue(liste_produits):
    cols = st.columns(3)
    for i, item in enumerate(liste_produits):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" style="width:100%; border-radius:10px;">
                    <h3 style="margin-top:15px; text-transform:uppercase;">{item['nom']}</h3>
                    <div class="price-tag">{item['prix']} FCFA</div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"COMMANDER {item['nom']}", f"https://wa.me/221XXXXXXXXX?text=Bonjour%20Avenir%20Sport,%20je%20veux%20commander%20:{item['nom']}")
            st.write("")

# --- CONTENU DES ONGLETS ---
with tab_home:
    st.markdown('<div class="rayon-banner">★ LES INCONTOURNABLES</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1511886929837-399a8a11bdca?q=80&w=2000")
    st.write("### Pourquoi choisir Avenir Sport Joal ?")
    c1, c2, c3 = st.columns(3)
    c1.metric("Clients Satisfaits", "500+", "+12%")
    c2.metric("Articles en Stock", "1200", "Nouveautés")
    c3.metric("Livraison", "Joal/Dakar", "24h")

with tab_maillots:
    st.markdown('<div class="rayon-banner">RAYON MAILLOTS OFFICIELS</div>', unsafe_allow_html=True)
    afficher_catalogue(MAILLOTS)

with tab_shoes:
    st.markdown('<div class="rayon-banner">RAYON CHAUSSURES & CRAMPONS</div>', unsafe_allow_html=True)
    afficher_catalogue(CHAUSSURES)

with tab_habits:
    st.markdown('<div class="rayon-banner">RAYON VÊTEMENTS DE SPORT</div>', unsafe_allow_html=True)
    afficher_catalogue(HABITS)
