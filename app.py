import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. CONFIGURATION DU NOYAU ---
st.set_page_config(
    page_title="AVENIR SPORT | Elite Global ERP",
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
        font-family: 'Orbitron', sans-serif; font-size: clamp(40px, 8vw, 100px) !important;
        font-weight: 900; color: var(--neon-gold); letter-spacing: 15px;
        text-shadow: 0 0 30px rgba(255, 218, 0, 0.5);
    }
    .product-box {
        background: #111; border-radius: 20px; overflow: hidden;
        border: 1px solid #222; transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 20px;
    }
    .product-box:hover { transform: translateY(-10px); border-color: var(--neon-gold); }
    .product-image { width: 100%; height: 300px; object-fit: cover; }
    .product-info { padding: 20px; background: linear-gradient(180deg, transparent, #000); }
    .badge-premium { background: var(--neon-gold); color: black; font-size: 10px; font-weight: 900; padding: 5px 12px; border-radius: 5px; }
    .price-big { font-family: 'Orbitron'; color: var(--neon-gold); font-size: 24px; margin-top: 10px; }
    .sidebar-monitor {
        background: rgba(255, 218, 0, 0.05); border: 1px solid var(--neon-gold);
        padding: 15px; border-radius: 12px; position: relative; overflow: hidden;
    }
    @keyframes scanline { 0% { top: 0%; } 100% { top: 100%; } }
    .sidebar-monitor::after {
        content: ""; position: absolute; width: 100%; height: 2px;
        background: var(--neon-gold); top: 0; left: 0; opacity: 0.2; animation: scanline 4s linear infinite;
    }
    .footer-matrix { background: #000; padding: 80px 40px; margin-top: 100px; border-top: 2px solid #333; }
</style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES MASSIVE (15 CATÉGORIES / 8 ITEMS PAR CAT) ---
class AvenirDatabase:
    def __init__(self):
        self.categories = {
            "ELITE KITS": [
                {"id": 101, "name": "Senegal Home 24/25", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=400", "desc": "Authentic Player Version."},
                {"id": 102, "name": "Real Madrid Home Pro", "price": 18500, "genre": "Homme", "stock": "5 restants", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=400", "desc": "Édition Champions League."},
                {"id": 103, "name": "France 2 étoiles Edition", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1551233869-adc2e0066ec9?w=400", "desc": "Coupe Euro 2024."},
                {"id": 104, "name": "Manchester City Third", "price": 17000, "genre": "Homme", "stock": "10 restants", "img": "https://images.unsplash.com/photo-1521233519344-93333454b03a?w=400", "desc": "Design Puma Ultra-breathable."},
                {"id": 105, "name": "Inter Miami Pink Messi", "price": 20000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1621938340478-f3da7e43689f?w=400", "desc": "Officiel MLS Edition."},
                {"id": 106, "name": "Arsenal Away Yellow", "price": 15000, "genre": "Unisexe", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1580460814612-70f90e9cc88e?w=400", "desc": "Adidas Heat-Ready."},
                {"id": 107, "name": "FC Barcelone Home 25", "price": 18000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=400", "desc": "Maillot Nike Stadium."},
                {"id": 108, "name": "Al Nassr Home CR7", "price": 19000, "genre": "Unisex", "stock": "Dernières unités", "img": "https://images.unsplash.com/photo-1631198094170-9856a59bc6ae?w=400", "desc": "Version championnat Saoudien."}
            ],
            "FOOTWEAR TECH": [
                {"id": 201, "name": "Mercurial Vapor 15 Elite", "price": 45000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", "desc": "Crampons FG Pro."},
                {"id": 202, "name": "Adidas Predator Acc.", "price": 42000, "genre": "Homme", "stock": "Dernière paire", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400", "desc": "Zone skin precision."},
                {"id": 203, "name": "Puma Future Ultimate", "price": 38000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400", "desc": "Fuzionfit+ technology."},
                {"id": 204, "name": "Phantom GX Elite", "price": 48000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400", "desc": "Technologie Gripknit."},
                {"id": 205, "name": "Mizuno Morelia Neo IV", "price": 55000, "genre": "Unisex", "stock": "3 paires", "img": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=400", "desc": "K-Leather Premium."},
                {"id": 206, "name": "Copa Mundial Classic", "price": 35000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Légende du football."},
                {"id": 207, "name": "Nike Tiempo Legend X", "price": 40000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1575537302964-96cd47c06b1b?w=400", "desc": "Flytouch Plus cuir synthétique."},
                {"id": 208, "name": "New Balance Tekela v4", "price": 42000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400", "desc": "Hypoknit sans lacets."}
            ],
            "PRO ACCESSORIES": [
                {"id": 301, "name": "Protège-Tibias Carbon X", "price": 9500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Protection ultra-légère."},
                {"id": 302, "name": "Chaussettes G-Grip Pro", "price": 4500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=400", "desc": "Antidérapantes stabilité."},
                {"id": 303, "name": "Gants Gardien Vapor", "price": 12000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=400", "desc": "Latex contact pro."},
                {"id": 304, "name": "Brassard Capitaine Custom", "price": 2500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1519751138087-5bf79df62d5b?w=400", "desc": "Élastique haute densité."},
                {"id": 305, "name": "Ruban Cheville Pro Tape", "price": 1500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?w=400", "desc": "Maintien ligamentaire."},
                {"id": 306, "name": "Sac de sport Avenir Pro", "price": 18000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400", "desc": "Compartiment chaussures."},
                {"id": 307, "name": "Pompe à ballon Digital", "price": 8500, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1526401485004-46910ecc8e51?w=400", "desc": "Mesure PSI précise."},
                {"id": 308, "name": "Bouteille Isotherme 1L", "price": 6000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1523362628242-f513a5e334f1?w=400", "desc": "Garde au frais 12h."}
            ],
            "TRAINING GEAR": [
                {"id": 401, "name": "Veste Coupe-vent Elite", "price": 25000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1556910602-38f30689260a?w=400", "desc": "Waterproof training gear."},
                {"id": 402, "name": "Short de training Mesh", "price": 8000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400", "desc": "Ultra léger."},
                {"id": 403, "name": "Haut de compression LS", "price": 12000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400", "desc": "Support musculaire."},
                {"id": 404, "name": "Leggings Sport Performance", "price": 14000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400", "desc": "Squat-proof fabric."},
                {"id": 405, "name": "Brassière High Impact", "price": 10000, "genre": "Femme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1548330065-2946a3426d73?w=400", "desc": "Maintien optimal."},
                {"id": 406, "name": "Jogging Tech-Fleece", "price": 22000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1515444744559-7be63e1600de?w=400", "desc": "Confort et style."},
                {"id": 407, "name": "Débardeur Run-Dry", "price": 6000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400", "desc": "Évacuation sueur."},
                {"id": 408, "name": "Chasubles d'entrainement", "price": 3000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1434608519344-49d77a699e1d?w=400", "desc": "Haute visibilité."}
            ],
            # ... (Ajoutez d'autres catégories ici sur le même modèle)
        }
        # Simulation pour arriver à 15 catégories (remplissage automatique)
        extra_cats = ["GOALKEEPER", "BASKETBALL", "LIFESTYLE", "SWIMWEAR", "GYM TOOLS", "KIDS ELITE", "RETRO CLASSICS", "RECOVERY", "COACHING", "NUTRITION", "OUTDOOR"]
        for cat in extra_cats:
            self.categories[cat] = [
                {"id": 999, "name": f"Produit {cat} Pro", "price": 12000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1518481612222-68bbe828ecd1?w=400", "desc": f"Equipement spécialisé pour {cat}."}
            ] * 8

db = AvenirDatabase()

# --- 4. SIDEBAR CONTROL PANEL ---
with st.sidebar:
    st.markdown("""<div class="sidebar-monitor">
        <h3 style="color:#ffda00; margin:0; font-family:Orbitron; font-size:16px;">🛰️ CONTROL PANEL</h3>
        <hr style="border-color:rgba(255,218,0,0.2);">
        <p style="font-size:11px; margin:0;">SYSTEM: ACTIVE 🟢</p>
        <p style="font-size:11px; margin:0;">Uptime: 99.9%</p>
    </div>""", unsafe_allow_html=True)
    st.divider()
    view_mode = st.radio("SÉLECTIONNER INTERFACE", ["🌐 CATALOGUE CLIENT", "🔐 GESTION STOCK (ERP)"])
    st.divider()
    st.info("HUB JOAL: 24/7 ONLINE")

# --- 5. INTERFACE CATALOGUE ---
if view_mode == "CATALOGUE CLIENT":
    st.markdown('<div class="hero-container"><h1 class="glitch-title">AVENIR SPORT</h1><p style="color:white; letter-spacing:10px;">GLOBAL PERFORMANCE SYSTEM</p></div>', unsafe_allow_html=True)
    
    selected_cat = st.selectbox("CHOISIR UNE CATÉGORIE", list(db.categories.keys()))
    st.markdown(f"<h2 style='color:#ffda00; font-family:Orbitron;'>// {selected_cat}</h2>", unsafe_allow_html=True)
    
    products = db.categories[selected_cat]
    cols = st.columns(4) # 4 colonnes pour plus de densité
    
    for i, item in enumerate(products):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="product-box">
                    <img src="{item['img']}" class="product-image">
                    <div class="product-info">
                        <span class="badge-premium">{item['genre']}</span>
                        <p style="color:#666; font-size:11px; margin:10px 0 0 0;">REF: AS-{item['id']}-{i}</p>
                        <h4 style="color:white; margin:5px 0;">{item['name']}</h4>
                        <div class="price-big">{item['price']:,} F</div>
                        <p style="color:#2ecc71; font-size:11px;">● {item['stock']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"COMMANDER VIA WHATSAPP", f"https://wa.me/221770953766?text=Bonjour,%20je%20souhaite%20commander%20l'article%20AS-{item['id']}")
            st.write("")

else: # --- MODE ERP ---
    st.title("🛡️ NEURAL ERP COMMAND")
    all_data = []
    for cat, items in db.categories.items():
        for i in items:
            all_data.append({"Catégorie": cat, "Nom": i['name'], "Prix": i['price'], "Stock": i['stock']})
    df = pd.DataFrame(all_data)
    st.dataframe(df, use_container_width=True)
    st.metric("NOMBRE D'ARTICLES", len(df), "+15 New")

# --- 6. FOOTER ---
st.markdown("""
    <div class="footer-matrix">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px; text-align: left;">
            <div><h4 style="color:#ffda00;">AVENIR_CORP</h4><p style="color:#666; font-size:12px;">Joal-Fadiouth, Sénégal.</p></div>
            <div><h4 style="color:#ffda00;">LOGISTIQUE</h4><p style="color:#666; font-size:12px;">Livraison Express 24H.</p></div>
            <div><h4 style="color:#ffda00;">SUPPORT</h4><p style="color:#666; font-size:12px;">WhatsApp: +221 77 095 37 66</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)
