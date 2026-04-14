import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. CONFIGURATION DU MOTEUR ---
st.set_page_config(
    page_title="AVENIR SPORT | Elite ERP System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. SYSTÈME DE DESIGN "CYBER-GOLD" (CSS TOTAL) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;700&display=swap');

    /* Variables Globales */
    :root {
        --neon-gold: #ffda00;
        --dark-bg: #050505;
        --glass: rgba(255, 255, 255, 0.03);
    }

    .stApp {
        background-color: var(--dark-bg);
        background-image: 
            linear-gradient(rgba(255, 218, 0, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 218, 0, 0.02) 1px, transparent 1px);
        background-size: 50px 50px;
    }

    /* En-tête Dynamique */
    .hero-container {
        padding: 60px;
        text-align: center;
        background: linear-gradient(180deg, rgba(255,218,0,0.1) 0%, transparent 100%);
        border-radius: 0 0 50px 50px;
        border-bottom: 2px solid var(--neon-gold);
        margin-bottom: 50px;
    }

    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 120px !important;
        font-weight: 900;
        color: var(--neon-gold);
        text-transform: uppercase;
        letter-spacing: 15px;
        line-height: 1;
        margin: 0;
        text-shadow: 0 0 30px rgba(255, 218, 0, 0.5);
    }

    /* Grille de Navigation */
    .nav-card {
        background: var(--glass);
        border: 1px solid rgba(255, 218, 0, 0.1);
        padding: 20px;
        border-radius: 15px;
        transition: 0.3s;
        text-align: center;
    }

    .nav-card:hover {
        border-color: var(--neon-gold);
        box-shadow: 0 0 20px rgba(255, 218, 0, 0.2);
    }

    /* Cartes Produits E-Commerce Pro */
    .product-box {
        background: #111;
        border-radius: 20px;
        padding: 0px;
        overflow: hidden;
        border: 1px solid #222;
        transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .product-box:hover {
        transform: translateY(-10px);
        border-color: var(--neon-gold);
    }

    .product-image {
        width: 100%;
        height: 350px;
        object-fit: cover;
        transition: 0.5s;
    }

    .product-info {
        padding: 25px;
        background: linear-gradient(180deg, transparent, #000);
    }

    .badge-premium {
        background: var(--neon-gold);
        color: black;
        font-size: 10px;
        font-weight: 900;
        padding: 5px 15px;
        border-radius: 5px;
        text-transform: uppercase;
    }

    .price-big {
        font-family: 'Orbitron';
        color: var(--neon-gold);
        font-size: 30px;
        margin-top: 10px;
    }

    /* Footer Industriel */
    .footer-matrix {
        background: #000;
        padding: 100px 40px;
        margin-top: 150px;
        border-top: 2px solid #333;
        font-family: 'Inter';
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CORE LOGIC & DATABASE SYSTEM ---
class AvenirDatabase:
    def __init__(self):
        self.categories = {
            "ELITE KITS": [
                {"id": 101, "name": "Maillot Sénégal 2024 Home", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=600", "desc": "Authentic Player Version - Dri-FIT Adv technology."},
                {"id": 102, "name": "Real Madrid Home 24/25", "price": 18500, "genre": "Homme", "stock": "5 restants", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=600", "desc": "Édition Champions League avec patchs officiels."},
                {"id": 103, "name": "Ensemble Training Femme", "price": 22000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1518310323272-61949103175a?w=600", "desc": "Coupe aérodynamique pour performance maximale."}
            ],
            "FOOTWEAR TECH": [
                {"id": 201, "name": "Nike Mercurial Vapor 15", "price": 45000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600", "desc": "Crampons FG pour terrain sec/synthétique."},
                {"id": 202, "name": "Adidas Predator Accuracy", "price": 42000, "genre": "Homme", "stock": "Dernière paire", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=600", "desc": "Zone skin pour un contrôle de balle chirurgical."}
            ],
            "PRO ACCESSORIES": [
                {"id": 301, "name": "Protège-Tibias Carbon X", "price": 9500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=600", "desc": "Protection ultra-légère certifiée FIFA."},
                {"id": 302, "name": "Chaussettes Performance G-Grip", "price": 4500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=600", "desc": "Antidérapantes pour une stabilité totale."}
            ]
        }

db = AvenirDatabase()

# --- 4. NAVIGATION LÉGALE & SIDEBAR ---
with st.sidebar:
    st.markdown(f"## ⚡ AVENIR CONTROL PANEL")
    st.info(f"Serveur : Localhost / Dakar-JOAL\nStatut : Online 🟢")
    st.divider()
    search = st.text_input("🔍 Recherche par ID ou Nom")
    view_mode = st.radio("Affichage", ["Catalogue Client", "Gestion Stock (ERP)"])
    st.divider()
    st.write("© 2026 - Avenir Sport Systems v4.0.1")

# --- 5. INTERFACE UTILISATEUR (UX) ---
if view_mode == "Catalogue Client":
    # Hero Section
    st.markdown("""
        <div class="hero-container">
            <h1 class="glitch-title">AVENIR SPORT</h1>
            <p style='color:white; letter-spacing:10px; font-weight:100;'>THE FUTURE OF PERFORMANCE</p>
        </div>
    """, unsafe_allow_html=True)

    # Tabs de catégories
    selected_cat = st.selectbox("", list(db.categories.keys()))

    # Grille de Produits Dynamique
    st.markdown(f"<h2 style='color:#ffda00; font-family:Orbitron;'>// {selected_cat}</h2>", unsafe_allow_html=True)
    
    products = db.categories[selected_cat]
    cols = st.columns(3)
    
    for i, item in enumerate(products):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-box">
                    <img src="{item['img']}" class="product-image">
                    <div class="product-info">
                        <span class="badge-premium">{item['genre']}</span>
                        <p style="color:#666; font-size:12px; margin-top:10px;">REF: AS-{item['id']}</p>
                        <h3 style="color:white; font-family:'Inter'; margin-bottom:5px;">{item['name']}</h3>
                        <p style="color:#999; font-size:13px; line-height:1.2;">{item['desc']}</p>
                        <div class="price-big">{item['price']:,} F</div>
                        <p style="color:#2ecc71; font-size:12px;">● {item['stock']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"COMMANDER VIA WHATSAPP", f"https://wa.me/221XXXXXXXXX?text=Bonjour,%20je%20souhaite%20commander%20l'article%20AS-{item['id']}")
            st.write("")

else: # --- MODE ERP GESTION DE STOCK ---
    st.title("🛡️ SYSTÈME DE GESTION DES RÉSERVES")
    st.warning("Accès restreint aux administrateurs de Joal-Fadiouth.")
    
    # Transformation des données pour analyse
    all_data = []
    for cat, items in db.categories.items():
        for i in items:
            all_data.append({"Catégorie": cat, "Nom": i['name'], "Prix": i['price'], "Stock": i['stock']})
    
    df = pd.DataFrame(all_data)
    st.table(df)
    st.metric(label="Valeur totale du stock estimée", value="1.450.000 FCFA", delta="+12%")

# --- 6. FOOTER MASSIVE ---
st.markdown("""
    <div class="footer-matrix">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 50px;">
            <div style="max-width:300px;">
                <h3 style="color:#ffda00; font-family:Orbitron;">AVENIR_CORP</h3>
                <p style="font-size:14px; color:#666;">Leader de l'équipement sportif au Sénégal. Importation directe, qualité certifiée, logistique optimisée.</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">LOGISTIQUE</h4>
                <p style="font-size:13px;">HUB JOAL : 24/7<br>HUB DAKAR : Livraison 12H<br>HUB MBOUR : Livraison 24H</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">LEGAL</h4>
                <p style="font-size:13px;">Conditions Générales de Vente<br>Politique de Retour Elite<br>Mentions Légales</p>
            </div>
            <div>
                <h4 style="color:#ffda00;">RESEAUX SOCIAUX</h4>
                <p style="font-size:13px;">Instagram @avenirsport_elite<br>TikTok @avenirsport_joal<br>Facebook Avenir Sport Sénégal</p>
            </div>
        </div>
        <div style="text-align:center; margin-top:80px; opacity:0.3; font-size:10px;">
            SÉCURISÉ PAR AVENIR-SYSTEMS-SECURITY-PROTOCOL v4.0.1
        </div>
    </div>
""", unsafe_allow_html=True)
