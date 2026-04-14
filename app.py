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

# --- 2. SYSTÈME DE DESIGN "CYBER-GOLD" ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;700&display=swap');
    :root { --neon-gold: #ffda00; --dark-bg: #050505; --glass: rgba(255, 255, 255, 0.03); }
    .stApp {
        background-color: var(--dark-bg);
        background-image: linear-gradient(rgba(255, 218, 0, 0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 218, 0, 0.02) 1px, transparent 1px);
        background-size: 50px 50px;
    }
    .hero-container {
        padding: 60px; text-align: center;
        background: linear-gradient(180deg, rgba(255,218,0,0.1) 0%, transparent 100%);
        border-radius: 0 0 50px 50px; border-bottom: 2px solid var(--neon-gold);
        margin-bottom: 50px;
    }
    .glitch-title {
        font-family: 'Orbitron', sans-serif; font-size: 80px !important;
        font-weight: 900; color: var(--neon-gold); text-transform: uppercase;
        letter-spacing: 15px; line-height: 1; margin: 0;
        text-shadow: 0 0 30px rgba(255, 218, 0, 0.5);
    }
    .product-box {
        background: #111; border-radius: 20px; padding: 0px;
        overflow: hidden; border: 1px solid #222;
        transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 20px;
    }
    .product-box:hover { transform: translateY(-10px); border-color: var(--neon-gold); }
    .product-image { width: 100%; height: 350px; object-fit: cover; }
    .product-info { padding: 25px; background: linear-gradient(180deg, transparent, #000); }
    .badge-premium {
        background: var(--neon-gold); color: black; font-size: 10px;
        font-weight: 900; padding: 5px 15px; border-radius: 5px;
        text-transform: uppercase;
    }
    .price-big { font-family: 'Orbitron'; color: var(--neon-gold); font-size: 28px; margin-top: 10px; }
    .footer-matrix {
        background: #000; padding: 100px 40px; margin-top: 150px;
        border-top: 2px solid #333; font-family: 'Inter';
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CORE LOGIC & DATABASE (15 CATÉGORIES / 8 PRODUITS) ---
class AvenirDatabase:
    def __init__(self):
        # Initialisation manuelle des catégories clés avec diversité de genre
        self.categories = {
            "ELITE KITS": [
                {"id": 101, "name": "Sénégal Home 24/25", "price": 15000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=600", "desc": "Authentic Player Version."},
                {"id": 102, "name": "Real Madrid Home 24/25", "price": 18500, "genre": "Homme", "stock": "5 restants", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=600", "desc": "Édition Champions League."},
                {"id": 103, "name": "Ensemble Training Pro", "price": 22000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1518310323272-61949103175a?w=600", "desc": "Coupe aérodynamique performance."},
                {"id": 104, "name": "Kit Junior Barça", "price": 12000, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=600", "desc": "Maillot + Short enfant."},
                {"id": 105, "name": "Maillot Al Nassr CR7", "price": 15000, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1631198094170-9856a59bc6ae?w=400", "desc": "Edition Junior."},
                {"id": 106, "name": "Veste de Pluie Elite", "price": 25000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1556910602-38f30689260a?w=400", "desc": "Technologie imperméable."},
                {"id": 107, "name": "Top Compression Femme", "price": 14000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1548330065-2946a3426d73?w=400", "desc": "Maintien musculaire."},
                {"id": 108, "name": "Survêtement Sénégal", "price": 35000, "genre": "Homme", "stock": "3 restants", "img": "https://images.unsplash.com/photo-1434608519344-49d77a699e1d?w=400", "desc": "Full set training."}
            ],
            "FOOTWEAR TECH": [
                {"id": 201, "name": "Nike Mercurial Vapor 15", "price": 45000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600", "desc": "Crampons FG Pro."},
                {"id": 202, "name": "Adidas Predator Accuracy", "price": 42000, "genre": "Homme", "stock": "Dernière paire", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=600", "desc": "Zone skin contrôle."},
                {"id": 203, "name": "Running Pegasus Femme", "price": 38000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400", "desc": "Amorti React."},
                {"id": 204, "name": "Baskets Junior Sport", "price": 18000, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=400", "desc": "Confort école et sport."},
                {"id": 205, "name": "Phantom GX Elite", "price": 48000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400", "desc": "Gripknit technology."},
                {"id": 206, "name": "Mizuno Morelia Neo", "price": 55000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1575537302964-96cd47c06b1b?w=400", "desc": "K-Leather Premium."},
                {"id": 207, "name": "Chaussures Futsal", "price": 22000, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Semelle non-marquante."},
                {"id": 208, "name": "Crampons Femme Elite", "price": 42000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400", "desc": "Adapté morphologie féminine."}
            ],
            "PRO ACCESSORIES": [
                {"id": 301, "name": "Grip Socks Pro", "price": 4500, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=600", "desc": "Anti-dérapantes."},
                {"id": 302, "name": "Protège-Tibias Carbon", "price": 9500, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=600", "desc": "Taille XS à L."},
                {"id": 303, "name": "Gants Gardien Vapor", "price": 12000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=400", "desc": "Latex contact pro."},
                {"id": 304, "name": "Bandeau Cheveux Sport", "price": 2500, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1519751138087-5bf79df62d5b?w=400", "desc": "Maintien élastique."},
                {"id": 305, "name": "Sac à dos Junior", "price": 15000, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400", "desc": "Multi-compartiments."},
                {"id": 306, "name": "Tape Médical", "price": 1500, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?w=400", "desc": "Support articulaire."},
                {"id": 307, "name": "Brass
