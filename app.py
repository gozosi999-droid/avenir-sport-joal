import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. CONFIGURATION DU NOYAU ---
st.set_page_config(
    page_title="AVENIR SPORT | GLOBAL INTERFACE",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DESIGN CYBER-GOLD (NETTOYÉ) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&family=Inter:wght@300;400;700&display=swap');
    :root { --neon-gold: #ffda00; --dark-bg: #050505; }
    .stApp {
        background-color: var(--dark-bg);
        background-image: linear-gradient(rgba(255, 218, 0, 0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 218, 0, 0.02) 1px, transparent 1px);
        background-size: 40px 40px;
    }
    .hero-container {
        padding: 50px; text-align: center;
        background: linear-gradient(180deg, rgba(255,218,0,0.1) 0%, transparent 100%);
        border-radius: 0 0 40px 40px; border-bottom: 2px solid var(--neon-gold);
        margin-bottom: 40px;
    }
    .glitch-title {
        font-family: 'Orbitron', sans-serif; font-size: clamp(35px, 7vw, 90px) !important;
        font-weight: 900; color: var(--neon-gold); letter-spacing: 12px;
        text-shadow: 0 0 25px rgba(255, 218, 0, 0.4);
    }
    .product-box {
        background: #111; border-radius: 15px; overflow: hidden;
        border: 1px solid #222; transition: 0.4s ease; margin-bottom: 15px;
    }
    .product-box:hover { transform: translateY(-8px); border-color: var(--neon-gold); box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    .product-image { width: 100%; height: 260px; object-fit: cover; }
    .product-info { padding: 18px; background: linear-gradient(180deg, transparent, #000); }
    .badge-premium { background: var(--neon-gold); color: black; font-size: 9px; font-weight: 900; padding: 4px 10px; border-radius: 4px; }
    .price-big { font-family: 'Orbitron'; color: var(--neon-gold); font-size: 22px; font-weight: 900; margin-top: 8px; }
    .footer-matrix { background: #000; padding: 60px 20px; border-top: 2px solid #222; text-align: center; margin-top: 80px; }
</style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES ULTRA-COMPLÈTE (15 CATÉGORIES) ---
class AvenirDatabase:
    def __init__(self):
        self.categories = {
            "ELITE KITS": [
                {"id": 101, "name": "Sénégal Home 24/25", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=400", "desc": "Qualité Thaïlande AAA."},
                {"id": 102, "name": "Real Madrid Home Pro", "price": 18500, "genre": "Homme", "stock": "5 restants", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=400", "desc": "Patchs UCL inclus."},
                {"id": 103, "name": "France 2 étoiles Euro", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1551233869-adc2e0066ec9?w=400", "desc": "Version Stadium."},
                {"id": 104, "name": "Man City Third Kit", "price": 17000, "genre": "Homme", "stock": "10 restants", "img": "https://images.unsplash.com/photo-1521233519344-93333454b03a?w=400", "desc": "Puma Ultraweave."},
                {"id": 105, "name": "Inter Miami Messi", "price": 20000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1621938340478-f3da7e43689f?w=400", "desc": "Édition Limitée Rose."},
                {"id": 106, "name": "Arsenal Away Yellow", "price": 15000, "genre": "Unisexe", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1580460814612-70f90e9cc88e?w=400", "desc": "Adidas Authentic."},
                {"id": 107, "name": "Barça Home 25", "price": 18000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=400", "desc": "Nike Dri-FIT."},
                {"id": 108, "name": "Al Nassr CR7", "price": 19000, "genre": "Unisex", "stock": "Dernières unités", "img": "https://images.unsplash.com/photo-1631198094170-9856a59bc6ae?w=400", "desc": "Version Jaune/Bleu."}
            ],
            "FOOTWEAR TECH": [
                {"id": 201, "name": "Mercurial Vapor 15", "price": 45000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", "desc": "Vitesse explosive."},
                {"id": 202, "name": "Adidas Predator", "price": 42000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400", "desc": "Contrôle total."},
                {"id": 203, "name": "Puma Future Ult.", "price": 38000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400", "desc": "Agilité extrême."},
                {"id": 204, "name": "Phantom GX Elite", "price": 48000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400", "desc": "Gripknit Pro."},
                {"id": 205, "name": "Nike Tiempo X", "price": 40000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1575537302964-96cd47c06b1b?w=400", "desc": "Cuir premium."},
                {"id": 206, "name": "Copa Mundial", "price": 35000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Classique éternel."},
                {"id": 207, "name": "NB Tekela v4", "price": 42000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400", "desc": "Zéro lacets."},
                {"id": 208, "name": "Mizuno Neo IV", "price": 55000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=400", "desc": "Fait main Japon."}
            ],
            "PRO ACCESSORIES": [
                {"id": 301, "name": "Grip Socks Elite", "price": 4500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=400", "desc": "Anti-glisse."},
                {"id": 302, "name": "Protège-Tibias Carbon", "price": 9500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Poids plume."},
                {"id": 303, "name": "Gants Gardien Pro", "price": 12000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=400", "desc": "Latex allemand."},
                {"id": 304, "name": "Sac Avenir Elite", "price": 18000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400", "desc": "Waterproof."},
                {"id": 305, "name": "Tape Médical Pro", "price": 1500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?w=400", "desc": "Support articulaire."},
                {"id": 306, "name": "Pompe Digitale", "price": 8500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1526401485004-46910ecc8e51?w=400", "desc": "Précision PSI."},
                {"id": 307, "name": "Brassard Capitaine", "price": 2500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1519751138087-5bf79df62d5b?w=400", "desc": "Élastique Pro."},
                {"id": 308, "name": "Bouteille Isotherme", "price": 6000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1523362628242-f513a5e334f1?w=400", "desc": "Inox Sport."}
            ],
            "TRAINING GEAR": [
                {"id": 401, "name": "Short Mesh Tech", "price": 8000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400", "desc": "Respirant."},
                {"id": 402, "name": "Compression Top", "price": 12000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400", "desc": "Muscle support."},
                {"id": 403, "name": "Brassière Pro", "price": 10000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1548330065-2946a3426d73?w=400", "desc": "Maintien fort."},
                {"id": 404, "name": "Leggings Sport", "price": 14000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400", "desc": "Anti-transpiration."},
                {"id": 405, "name": "Veste Coupe-vent", "price": 25000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1556910602-38f30689260a?w=400", "
