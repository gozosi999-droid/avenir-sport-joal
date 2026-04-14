import streamlit as st
import os

# 1. CONFIGURATION
st.set_page_config(page_title="Avenir Sport Joal | Boutique Elite", layout="wide")

# --- DESIGN CSS PRO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;500;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.85)), 
                    url("https://images.unsplash.com/photo-1534158914592-062992fbe900?q=80&w=2000");
        background-size: cover;
        background-attachment: fixed;
    }

    .titre-sport {
        font-family: 'Bebas Neue';
        font-size: 110px !important;
        background: linear-gradient(180deg, #ffda00 0%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        text-transform: uppercase;
        font-style: italic;
        filter: drop-shadow(4px 4px 2px #000);
    }

    /* Style des Onglets Texture Or/Verre */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: rgba(255, 218, 0, 0.05);
        border-radius: 12px 12px 0 0;
        color: white !important;
        font-family: 'Bebas Neue';
        font-size: 20px;
        border: 1px solid rgba(255, 218, 0, 0.2);
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffda00 !important;
        color: black !important;
    }

    .product-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: black;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    .price-tag {
        background: #000;
        color: #ffda00;
        font-weight: bold;
        padding: 5px 15px;
        border-radius: 5px;
        display: inline-block;
        margin: 10px 0;
    }

    .footer-xxl {
        background: #000;
        color: white;
        padding: 60px;
        border-top: 8px solid #ffda00;
        margin-top: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DONNÉES ÉTENDUE (On allonge le code ici)
RAYON_MAILLOTS = [
    {"nom": "Sénégal Home 2024", "prix": "15.000", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?q=80&w=400"},
    {"nom": "Sénégal Away 2024", "prix": "15.000", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?q=80&w=400"},
    {"nom": "Real Madrid Home", "prix": "18.500", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?q=80&w=400"},
    {"nom": "FC Barcelone", "prix": "18.500", "img": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?q=80&w=400"},
    {"nom": "Manchester City", "prix": "17.000", "img": "https://images.unsplash.com/photo-1589487391730-58f20eb2c308?q=80&w=400"},
    {"nom": "Arsenal Home", "prix": "17.500", "img": "https://images.unsplash.com/photo-1521731902048-96593a12a322?q=80&w=400"},
    {"nom": "PSG Jordan", "prix": "18.000", "img": "https://images.unsplash.com/photo-1614632537190-23e444104533?q=80&w=400"},
    {"nom": "Equipe de France", "prix": "16.500", "img": "https://images.unsplash.com/photo-1551952237-954a0e68786c?q=80&w=400"},
    {"nom": "Brésil Classic", "prix": "15.500", "img": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=400"}
]

RAYON_SHOES = [
    {"nom": "Nike Mercurial Pro", "prix": "35.000", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=400"},
    {"nom": "Adidas Predator", "prix": "32.000", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?q=80&w=400"},
    {"nom": "Puma Future", "prix": "29.000", "img": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?q=80&w=400"},
    {"nom": "Nike Phantom GX", "prix": "38.000", "img": "https://images.unsplash.com/photo-1511556532299-8f662fc26c06?q=80&w=400"},
    {"nom": "Nike Air Max Sport", "prix": "45.000", "img": "https://images.unsplash.com/photo-1514989940723-e8e51635b782?q=80&w=400"}
]

# 3. INTERFACE
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("logo.png"): st.image("logo.png", width=180)
with col2:
    st.markdown('<h1 class="titre-sport">AVENIR SPORT</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ffda00; letter-spacing:10px;'>ELITE JOAL PERFORMANCE</p>", unsafe_allow_html=True)

tab_home, tab_maillots, tab_shoes, tab_contact = st.tabs(["🏠 ACCUEIL", "👕 MAILLOTS", "👟 CHAUSSURES", "📞 CONTACT"])

def draw_grid(items):
    cols = st.columns(3)
    for i, item in enumerate(items):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" style="width:100%; border-radius:10px;">
                    <h3>{item['nom']}</h3>
                    <div class="price-tag">{item['prix']} FCFA</div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"COMMANDER {item['nom']}", "https://wa.me/221XXXXXXXXX")

with tab_home:
    st.image("https://images.unsplash.com/photo-1543326727-cf6c39e8f84c?q=80&w=2000")
    st.markdown("## Bienvenue chez le n°1 à Joal-Fadiouth")

with tab_maillots:
    draw_grid(RAYON_MAILLOTS)

with tab_shoes:
    draw_grid(RAYON_SHOES)

with tab_contact:
    st.markdown("""
        <div style="background:rgba(255,255,255,0.1); padding:40px; border-radius:20px; color:white;">
            <h2>📞 NOS CONTACTS</h2>
            <p>Téléphone : +221 77 XXX XX XX</p>
            <p>WhatsApp : [Lien direct](https://wa.me/221XXXXXXXXX)</p>
            <p>Adresse : Joal-Fadiouth, Sénégal</p>
        </div>
    """, unsafe_allow_html=True)

# 4. FOOTER XXL (Correction du caractère °)
st.markdown("""
    <div class="footer-xxl">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px;">
            <div>
                <h2 style="color:#ffda00;">AVENIR SPORT JOAL</h2>
                <p>La destination Numero 1 pour les passionnes de foot.<br>Qualite superieure garantie.</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">RAYONS</h4>
                <p>Maillots Clubs</p><p>Equipe Nationale</p><p>Chaussures</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">RÉSEAUX</h4>
                <p>Instagram : @avenirsport_joal</p><p>Facebook : Avenir Sport Joal</p>
            </div>
        </div>
        <hr style="border-color: #333; margin: 40px 0;">
        <p style="text-align: center; opacity: 0.4;">© 2026 AVENIR SPORT JOAL - Site Officiel.</p>
    </div>
    """, unsafe_allow_html=True)
