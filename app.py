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
                {"id": 307, "name": "Brassard Capitaine", "price": 2500, "genre": "Enfants", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1519751138087-5bf79df62d5b?w=400", "desc": "Taille ajustable."},
                {"id": 308, "name": "Genouillères Volley", "price": 8500, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Protection impact."}
            ]
        }
        
        # Ajout automatique des 12 autres catégories pour atteindre 15
        extra_cats = ["BASKETBALL", "GYM & FITNESS", "SWIMWEAR", "BOXE", "RETRO CLASSIC", "NUTRITION", "RECOVERY", "COACHING", "LIFESTYLE", "YOGA", "OUTDOOR", "TENNIS"]
        for cat in extra_cats:
            self.categories[cat] = [
                {"id": 999, "name": f"Produit {cat} Pro", "price": 10000, "genre": g, "stock": "En Stock", "img": "https://images.unsplash.com/photo-1518481612222-68bbe828ecd1?w=400", "desc": "Performance garantie."}
                for g in ["Homme", "Femme", "Enfants", "Homme", "Femme", "Enfants", "Homme", "Femme"]
            ]

db = AvenirDatabase()

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown(f"## ⚡ AVENIR CONTROL PANEL")
    st.info(f"HUB : Dakar-JOAL\nStatut : Online 🟢")
    st.divider()
    view_mode = st.radio("SÉLECTIONNER INTERFACE", ["Catalogue Client", "Gestion Stock (ERP)"])
    st.divider()
    
    # Filtres de genre uniquement pour le catalogue
    if view_mode == "Catalogue Client":
        st.write("🎯 FILTRER PAR CIBLE")
        filter_genre = st.multiselect("Genres", ["Homme", "Femme", "Enfants"], default=["Homme", "Femme", "Enfants"])
    
    st.write("© 2026 - Avenir Sport v5.0")

# --- 5. INTERFACE CLIENT ---
if view_mode == "Catalogue Client":
    st.markdown("""
        <div class="hero-container">
            <h1 class="glitch-title">AVENIR SPORT</h1>
            <p style='color:white; letter-spacing:10px;'>ELITE PERFORMANCE SYSTEM</p>
        </div>
    """, unsafe_allow_html=True)

    selected_cat = st.selectbox("CHOISIR UNE CATÉGORIE", list(db.categories.keys()))
    
    # Filtrage des produits selon le genre sélectionné en sidebar
    products = [p for p in db.categories[selected_cat] if p['genre'] in filter_genre]
    
    st.markdown(f"<h2 style='color:#ffda00; font-family:Orbitron;'>// {selected_cat} ({len(products)})</h2>", unsafe_allow_html=True)
    
    if not products:
        st.warning("Aucun produit ne correspond à ces filtres pour cette catégorie.")
    else:
        cols = st.columns(3)
        for i, item in enumerate(products):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="product-box">
                        <img src="{item['img']}" class="product-image">
                        <div class="product-info">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span class="badge-premium">{item['genre']}</span>
                                <small style="color:#666;">REF: AS-{item['id']}</small>
                            </div>
                            <h3 style="color:white; font-family:'Inter'; margin:15px 0 5px 0;">{item['name']}</h3>
                            <p style="color:#999; font-size:13px; height:40px; overflow:hidden;">{item['desc']}</p>
                            <div class="price-big">{item['price']:,} F</div>
                            <p style="color:#2ecc71; font-size:12px; margin-top:5px;">● {item['stock']}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"COMMANDER WHATSAPP", f"https://wa.me/221770953766?text=Bonjour,%20je%20souhaite%20commander%20l'article%20AS-{item['id']} ({item['name']})")
                st.write("")

else: # --- MODE ERP ---
    st.title("🛡️ GESTION DU STOCK CENTRAL")
    all_data = []
    for cat, items in db.categories.items():
        for i in items:
            all_data.append({"Catégorie": cat, "Nom": i['name'], "Genre": i['genre'], "Prix": i['price'], "Stock": i['stock']})
    
    df = pd.DataFrame(all_data)
    st.dataframe(df, use_container_width=True)
    st.metric("NOMBRE D'ARTICLES RÉFÉRENCÉS", len(df), "+120")

# --- 6. FOOTER ---
st.markdown("""
    <div class="footer-matrix">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 50px; text-align:left;">
            <div><h4 style="color:#ffda00;">LOGISTIQUE</h4><p style="font-size:13px; color:#999;">HUB JOAL : 24/7<br>HUB DAKAR : Livraison 12H</p></div>
            <div><h4 style="color:#ffda00;">RESEAUX</h4><p style="font-size:13px; color:#999;">Instagram @avenirsport<br>TikTok @avenirsport</p></div>
            <div><h4 style="color:#ffda00;">SYSTEM</h4><p style="font-size:13px; color:#999;">Version 5.0 Stable<br>Joal-Fadiouth, SN</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)
