import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="AVENIR SPORT | Elite ERP System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DESIGN CYBER-GOLD ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;700&display=swap');
    :root { --neon-gold: #ffda00; --dark-bg: #050505; }
    .stApp { background-color: var(--dark-bg); color: white; }
    .hero-container {
        padding: 40px; text-align: center;
        background: linear-gradient(180deg, rgba(255,218,0,0.1) 0%, transparent 100%);
        border-bottom: 2px solid var(--neon-gold); margin-bottom: 30px;
    }
    .glitch-title { font-family: 'Orbitron'; font-size: 60px; color: var(--neon-gold); letter-spacing: 10px; }
    .product-box {
        background: #111; border-radius: 15px; border: 1px solid #222;
        padding: 0px; overflow: hidden; transition: 0.3s;
    }
    .product-box:hover { border-color: var(--neon-gold); transform: translateY(-5px); }
    .product-image { width: 100%; height: 250px; object-fit: cover; }
    .product-info { padding: 15px; }
    .price-tag { font-family: 'Orbitron'; color: var(--neon-gold); font-size: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES (15 CATÉGORIES X 8 PRODUITS) ---
class AvenirDatabase:
    def __init__(self):
        # Fonction pour générer 8 produits par catégorie facilement
        def gen_items(cat_name, base_price, start_id):
            return [
                {"id": start_id + i, "name": f"{cat_name} Model-{i+1}", "price": base_price + (i*500), "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=400", "desc": "Performance Elite."}
                for i in range(8)
            ]

        self.categories = {
            "ELITE KITS": [
                {"id": 101, "name": "Sénégal Home 24/25", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=400", "desc": "Qualité AAA."},
                {"id": 102, "name": "Real Madrid Home", "price": 18500, "genre": "Homme", "stock": "5 restants", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=400", "desc": "Patchs UCL."},
                {"id": 103, "name": "Barça Home 25", "price": 18000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=400", "desc": "Nike Dri-FIT."},
                {"id": 104, "name": "Man City Third", "price": 17000, "genre": "Homme", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1521233519344-93333454b03a?w=400", "desc": "Puma Ultraweave."},
                {"id": 105, "name": "France Euro 24", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1551233869-adc2e0066ec9?w=400", "desc": "Stadium Edition."},
                {"id": 106, "name": "Arsenal Yellow", "price": 15000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1580460814612-70f90e9cc88e?w=400", "desc": "Adidas Authentic."},
                {"id": 107, "name": "Inter Miami Messi", "price": 20000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1621938340478-f3da7e43689f?w=400", "desc": "Limited Pink."},
                {"id": 108, "name": "Al Nassr CR7", "price": 19000, "genre": "Unisex", "stock": "En Stock", "img": "https://images.unsplash.com/photo-1631198094170-9856a59bc6ae?w=400", "desc": "Sidi Edition."}
            ],
            "FOOTWEAR TECH": gen_items("Crampon Pro", 35000, 200),
            "PRO ACCESSORIES": gen_items("Accessoire", 4500, 300),
            "TRAINING GEAR": gen_items("Training", 12000, 400),
            "BASKETBALL ZONE": gen_items("Basket", 45000, 500),
            "GYM & FITNESS": gen_items("Gym", 8000, 600),
            "GOALKEEPER": gen_items("Gants/Protec", 15000, 700),
            "LIFESTYLE": gen_items("Streetwear", 18000, 800),
            "RETRO CLASSICS": gen_items("Vintage", 25000, 900),
            "SWIMWEAR": gen_items("Natation", 10000, 1000),
            "KIDS ELITE": gen_items("Enfant", 12000, 1100),
            "NUTRITION": gen_items("Protein/Supp", 25000, 1200),
            "RECOVERY": gen_items("Massage/Recovery", 35000, 1300),
            "COACHING": gen_items("Coach Tools", 5000, 1400),
            "OUTDOOR": gen_items("Rando/Trail", 30000, 1500)
        }

db = AvenirDatabase()

# --- 4. NAVIGATION ---
with st.sidebar:
    st.markdown('<h2 style="color:#ffda00;">⚡ AVENIR CONTROL</h2>', unsafe_allow_html=True)
    mode = st.radio("Interface", ["Catalogue", "Gestion Stock"])
    st.divider()
    st.write("Dakar-Joal Hub 🟢")

# --- 5. LOGIQUE ---
if mode == "Catalogue":
    st.markdown('<div class="hero-container"><h1 class="glitch-title">AVENIR SPORT</h1></div>', unsafe_allow_html=True)
    
    selected_cat = st.selectbox("Choisir Rayon", list(db.categories.keys()))
    items = db.categories[selected_cat]
    
    cols = st.columns(4)
    for i, item in enumerate(items):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="product-box">
                    <img src="{item['img']}" class="product-image">
                    <div class="product-info">
                        <small style="color:gray;">REF: AS-{item['id']}</small>
                        <h4 style="margin:5px 0;">{item['name']}</h4>
                        <div class="price-tag">{item['price']:,} F</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("COMMANDER", f"https://wa.me/221770953766?text=Commande_AS-{item['id']}")
            st.write("")
else:
    st.title("🛡️ Stock Management")
    all_rows = []
    for c, itms in db.categories.items():
        for i in itms:
            all_rows.append({"Cat": c, "Produit": i['name'], "Prix": i['price']})
    st.table(pd.DataFrame(all_rows))

# --- 6. FOOTER ---
st.markdown("<div style='text-align:center; padding:50px; border-top:1px solid #222; margin-top:50px;'>© 2026 AVENIR SPORT JOAL</div>", unsafe_allow_html=True)
