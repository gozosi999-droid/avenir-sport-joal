import streamlit as st
import os

# 1. CONFIGURATION
st.set_page_config(page_title="Avenir Sport Joal | Boutique Pro", layout="wide")

# --- STYLE CSS (LE LOOK CITY SPORT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@400;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url("https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=2000");
        background-size: cover;
        background-attachment: fixed;
    }

    .titre-sport {
        font-family: 'Bebas Neue';
        font-size: 100px !important;
        color: #ffda00; 
        text-align: center;
        text-transform: uppercase;
        font-style: italic;
        text-shadow: 4px 4px 0px #000000;
        margin-bottom: 0px;
    }

    .rayon-banner {
        background: linear-gradient(90deg, #ffda00 0%, #000000 100%);
        color: black;
        font-family: 'Bebas Neue';
        font-size: 35px;
        padding: 10px 30px;
        border-radius: 0 50px 50px 0;
        margin: 40px 0 20px 0;
    }

    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: black !important;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }

    .price-tag {
        background-color: #ffda00;
        color: black;
        font-weight: bold;
        font-size: 22px;
        padding: 5px 15px;
        border-radius: 5px;
        display: inline-block;
        margin: 10px 0;
    }

    .footer {
        background-color: #000;
        color: white;
        padding: 60px;
        margin-top: 100px;
        border-top: 5px solid #ffda00;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DONNÉES PRODUITS (AVEC VRAIES PHOTOS)
# Tu peux copier-coller ces lignes pour atteindre 1000+ articles
MAILLOTS = [
    {"nom": "Maillot Sénégal Officiel", "prix": "15.000", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?q=80&w=600"},
    {"nom": "Maillot Real Madrid Home", "prix": "18.000", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?q=80&w=600"},
    {"nom": "Maillot Barça 2025", "prix": "18.000", "img": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?q=80&w=600"},
    {"nom": "Maillot Man City", "prix": "17.500", "img": "https://images.unsplash.com/photo-1589487391730-58f20eb2c308?q=80&w=600"},
    {"nom": "Maillot PSG Jordan", "prix": "17.000", "img": "https://images.unsplash.com/photo-1614632537190-23e444104533?q=80&w=600"},
    {"nom": "Maillot Arsenal Home", "prix": "17.500", "img": "https://images.unsplash.com/photo-1521731902048-96593a12a322?q=80&w=600"}
]

CHAUSSURES = [
    {"nom": "Nike Mercurial Speed", "prix": "35.000", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=600"},
    {"nom": "Adidas Predator Elite", "prix": "32.000", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?q=80&w=600"},
    {"nom": "Puma Future Ultimate", "prix": "28.500", "img": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?q=80&w=600"}
]

# 3. AFFICHAGE
col_logo, col_titre = st.columns([1, 4])
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
with col_titre:
    st.markdown('<p class="titre-sport">AVENIR SPORT</p>', unsafe_allow_html=True)

# Navigation
tabs = st.tabs(["🏠 ACCUEIL", "👕 MAILLOTS", "👟 CHAUSSURES", "📞 CONTACT"])

# Logique d'affichage automatique
def dessiner_catalogue(liste):
    cols = st.columns(3)
    for i, p in enumerate(liste):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius:10px; height:200px; object-fit:cover;">
                    <h3 style="margin-top:10px;">{p['nom']}</h3>
                    <div class="price-tag">{p['prix']} F</div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"COMMANDER {p['nom']}", f"https://wa.me/221XXXXXXXXX")

with tabs[1]:
    st.markdown('<div class="rayon-banner">RAYON MAILLOTS</div>', unsafe_allow_html=True)
    dessiner_catalogue(MAILLOTS)

with tabs[2]:
    st.markdown('<div class="rayon-banner">RAYON CHAUSSURES</div>', unsafe_allow_html=True)
    dessiner_catalogue(CHAUSSURES)

# 4. FOOTER
st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: space-around;">
            <div><h3>AVENIR SPORT JOAL</h3><p>Joal-Fadiouth, Sénégal</p></div>
            <div><h3>CONTACT</h3><p>📞 +221 XX XXX XX XX</p><p>📧 contact@avenirsport.com</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
