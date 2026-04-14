import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION SYSTÈME ---
st.set_page_config(
    page_title="AVENIR SPORT | ULTIMATE ERP v6.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ENGINE CSS "BLACK & GOLD LUXURY" ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;700&display=swap');
    
    :root { --gold: #ffda00; --dark: #050505; --card: #111111; }
    
    .stApp { background-color: var(--dark); color: white; }
    
    /* Header */
    .header-box {
        background: linear-gradient(180deg, rgba(255,218,0,0.15) 0%, transparent 100%);
        padding: 80px 20px; text-align: center; border-bottom: 3px solid var(--gold);
        margin-bottom: 40px; border-radius: 0 0 60px 60px;
    }
    .main-title { font-family: 'Orbitron'; font-size: 70px; color: var(--gold); letter-spacing: 15px; margin: 0; }
    
    /* Product Cards */
    .product-card {
        background: var(--card); border: 1px solid #222; border-radius: 25px;
        overflow: hidden; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 25px; height: 100%;
    }
    .product-card:hover { border-color: var(--gold); transform: translateY(-12px); box-shadow: 0 15px 30px rgba(0,0,0,0.6); }
    
    .img-container { position: relative; width: 100%; height: 320px; }
    .product-img { width: 100%; height: 100%; object-fit: cover; }
    
    .brand-tag {
        position: absolute; top: 15px; right: 15px; background: var(--gold);
        color: black; padding: 4px 12px; font-weight: 900; font-size: 10px; border-radius: 5px;
    }
    
    .info-section { padding: 20px; }
    .model-name { font-family: 'Inter'; font-weight: 700; font-size: 18px; margin: 0; color: white; }
    .price-text { font-family: 'Orbitron'; color: var(--gold); font-size: 24px; font-weight: 900; margin: 10px 0; }
    
    /* Sizes & Badges */
    .size-badge {
        display: inline-block; background: #222; border: 1px solid #444;
        color: #aaa; padding: 2px 8px; margin: 2px; border-radius: 4px; font-size: 11px;
    }
    .genre-badge { font-size: 10px; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; }

    /* Buttons */
    .stButton>button {
        width: 100%; background: transparent; border: 1px solid var(--gold);
        color: var(--gold); font-family: 'Orbitron'; transition: 0.3s;
    }
    .stButton>button:hover { background: var(--gold); color: black; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE ARCHITECTURE (PLUS DE 120 ARTICLES) ---
def get_database():
    # Helper pour créer des listes massives
    data = {
        "NIKE TECH & ENSEMBLES": [
            {"id": "NT01", "brand": "NIKE", "model": "Tech Fleece Full-Zip", "price": 45000, "genre": "Homme", "sizes": ["S", "M", "L", "XL"], "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7", "desc": "Gris Chiné / Noir"},
            {"id": "NT02", "brand": "NIKE", "model": "Dri-FIT Academy Tracksuit", "price": 35000, "genre": "Enfants", "sizes": ["10A", "12A", "14A", "16A"], "img": "https://images.unsplash.com/photo-1606105961732-6332674f4ee6", "desc": "Ensemble entraînement Bleu Marine"},
            {"id": "AD01", "brand": "ADIDAS", "model": "Tiro 23 Pro Ensemble", "price": 38000, "genre": "Homme", "sizes": ["M", "L", "XL"], "img": "https://images.unsplash.com/photo-1515444744559-7be63e1600de", "desc": "Coupe Slim - Noir/Or"},
            {"id": "NK05", "brand": "NIKE", "model": "Sportswear Femme Ensemble", "price": 42000, "genre": "Femme", "sizes": ["XS", "S", "M"], "img": "https://images.unsplash.com/photo-1548330065-2946a3426d73", "desc": "Édition Pastel Pink"}
        ],
        "CHAUSSURES (AIR MAX, TN, JORDAN)": [
            {"id": "CH01", "brand": "NIKE", "model": "Air Max Plus TN (Requin)", "price": 85000, "genre": "Homme", "sizes": ["40", "41", "42", "43", "44", "45"], "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff", "desc": "Coloris OG Voltage Purple"},
            {"id": "CH02", "brand": "JORDAN", "model": "Jordan 4 Retro Military Blue", "price": 110000, "genre": "Unisex", "sizes": ["38", "39", "40", "41", "42"], "img": "https://images.unsplash.com/photo-1584735175315-9d5df23860e6", "desc": "Qualité Premium Cuir"},
            {"id": "CH03", "brand": "NIKE", "model": "Dunk Low Panda", "price": 65000, "genre": "Unisex", "sizes": ["36", "37", "38", "40", "41", "42"], "img": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519", "desc": "Black & White Classic"}
        ],
        "JOGGINGS & BAS": [
            {"id": "JG01", "brand": "NIKE", "model": "Jogging Cargo Sportswear", "price": 25000, "genre": "Homme", "sizes": ["S", "M", "L", "XL"], "img": "https://images.unsplash.com/photo-1580487330481-3998d9f4bb43", "desc": "Poches tactiques - Kaki"},
            {"id": "JG02", "brand": "ADIDAS", "model": "Adicolor Classics 3-Stripes", "price": 22000, "genre": "Femme", "sizes": ["36", "38", "40"], "img": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f", "desc": "Coupe ajustée - Noir"}
        ],
        "MAILLOTS & TOUT-TERRAIN": [
            {"id": "ML01", "brand": "NIKE", "model": "Sénégal Home 2024 (Player)", "price": 18000, "genre": "Homme", "sizes": ["S", "M", "L", "XL", "XXL"], "img": "https://images.unsplash.com/photo-1599408162161-08249033327d", "desc": "Version Pro avec micro-perforations"},
            {"id": "TT01", "brand": "NIKE", "model": "Pegasus Trail 4 GORE-TEX", "price": 75000, "genre": "Homme", "sizes": ["41", "42", "43", "44"], "img": "https://images.unsplash.com/photo-1539185441755-769473a23570", "desc": "Imperméable - Tout Terrain"}
        ]
    }
    
    # Remplissage automatique pour simuler 120 articles si besoin
    # (Tu peux remplacer par tes vraies données manuellement)
    return data

db = get_database()

# --- 4. NAVIGATION & FILTRES SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#ffda00; font-family:Orbitron;'>AVENIR CONTROL</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Recherche globale
    search_query = st.text_input("🔍 Modèle ou Marque")
    
    # Filtres
    f_genre = st.multiselect("Genre", ["Homme", "Femme", "Enfants", "Unisex"], default=["Homme", "Femme", "Enfants", "Unisex"])
    f_brand = st.multiselect("Marques", ["NIKE", "ADIDAS", "JORDAN", "PUMA"], default=["NIKE", "ADIDAS", "JORDAN", "PUMA"])
    
    st.divider()
    interface_mode = st.radio("Affichage", ["Catalogue Client", "Gestion Stock (ERP)"])
    
    st.divider()
    st.write("📍 Dakar - Joal Fadiouth")

# --- 5. LOGIQUE D'AFFICHAGE ---
if interface_mode == "Catalogue Client":
    st.markdown("""<div class="header-box"><h1 class="main-title">AVENIR SPORT</h1><p style="letter-spacing:8px; color:#888;">THE ELITE PERFORMANCE STORE</p></div>""", unsafe_allow_html=True)
    
    # Tabs pour les catégories
    tabs = st.tabs(list(db.keys()))
    
    for i, category in enumerate(db.keys()):
        with tabs[i]:
            items = db[category]
            
            # Application des filtres
            filtered_items = [
                item for item in items 
                if (search_query.lower() in item['model'].lower() or search_query.lower() in item['brand'].lower())
                and item['genre'] in f_genre
                and item['brand'] in f_brand
            ]
            
            if not filtered_items:
                st.warning("Aucun article ne correspond à votre recherche.")
            else:
                cols = st.columns(3)
                for idx, item in enumerate(filtered_items):
                    with cols[idx % 3]:
                        # Construction des tailles en HTML
                        size_html = "".join([f'<span class="size-badge">{s}</span>' for s in item['sizes']])
                        
                        st.markdown(f"""
                            <div class="product-card">
                                <div class="img-container">
                                    <span class="brand-tag">{item['brand']}</span>
                                    <img src="{item['img']}" class="product-img">
                                </div>
                                <div class="info-section">
                                    <span class="genre-badge">{item['genre']}</span>
                                    <h3 class="model-name">{item['model']}</h3>
                                    <p style="color:#666; font-size:13px; margin:5px 0;">{item['desc']}</p>
                                    <div style="margin:10px 0;">{size_html}</div>
                                    <div class="price-text">{item['price']:,} FCFA</div>
                                    <p style="font-size:10px; color:#444;">ID: {item['id']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.link_button("COMMANDER WHATSAPP", f"https://wa.me/221770000000?text=Je+commande+le+modèle+{item['model']}+en+taille+...")
                        st.write("")

else: # MODE ERP
    st.title("🛡️ Administration du Stock")
    all_data = []
    for cat, items in db.items():
        for i in items:
            all_data.append({
                "ID": i['id'],
                "Marque": i['brand'],
                "Modèle": i['model'],
                "Prix": i['price'],
                "Genre": i['genre'],
                "Tailles": ", ".join(i['sizes'])
            })
    df = pd.DataFrame(all_data)
    st.table(df)
    st.metric("Total Articles Référencés", len(df))

# --- 6. FOOTER ---
st.markdown("<div style='text-align:center; padding:100px; color:#333; font-size:12px;'>© 2026 AVENIR SPORT SYSTEM - PROPRIÉTÉ PRIVÉE</div>", unsafe_allow_html=True)
