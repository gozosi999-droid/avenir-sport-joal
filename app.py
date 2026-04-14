import streamlit as st
import pandas as pd

# --- 1. CONFIGURATION ÉLITE ---
st.set_page_config(
    page_title="AVENIR SPORT | GLOBAL LOGISTICS",
    page_icon="👟",
    layout="wide"
)

# --- 2. CSS CUSTOM : INTERFACE INDUSTRIELLE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    :root { --gold: #ffda00; --bg: #0a0a0a; --surface: #151515; }
    
    .stApp { background-color: var(--bg); color: #e0e0e0; }
    
    .main-header {
        background: linear-gradient(135deg, #1a1a1a 0%, #000 100%);
        padding: 60px; border-bottom: 4px solid var(--gold);
        text-align: center; border-radius: 0 0 40px 40px; margin-bottom: 40px;
    }

    .brand-card {
        background: var(--surface); border-radius: 20px;
        border: 1px solid #222; transition: 0.3s; height: 100%;
    }
    .brand-card:hover { border-color: var(--gold); transform: translateY(-5px); }
    
    .product-img { width: 100%; height: 300px; object-fit: cover; border-radius: 20px 20px 0 0; }
    
    .status-badge {
        padding: 4px 10px; border-radius: 4px; font-size: 10px; font-weight: bold;
        text-transform: uppercase; margin-bottom: 10px; display: inline-block;
    }
    
    .price-tag { font-family: 'Orbitron'; color: var(--gold); font-size: 24px; font-weight: bold; }
    
    .size-box {
        display: inline-block; width: 35px; height: 35px; line-height: 35px;
        text-align: center; border: 1px solid #333; margin: 2px;
        font-size: 11px; border-radius: 5px; background: #000;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ARCHITECTURE DE LA BASE DE DONNÉES ---
# Cette structure permet de classer par Marque > Catégorie > Produit
inventory = {
    "NIKE": {
        "JOGGING": [
            {"id": "NK-JG-01", "name": "Nike Tech Fleece Full-Kit", "genre": "Homme", "sizes": ["S", "M", "L", "XL"], "price": 45000, "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7", "stock": "DISPONIBLE"},
            {"id": "NK-JG-02", "name": "Pantalon Dri-FIT Academy", "genre": "Unisex", "sizes": ["M", "L", "XXL"], "price": 25000, "img": "https://images.unsplash.com/photo-1580487330481-3998d9f4bb43", "stock": "DISPONIBLE"}
        ],
        "MAILLOTS": [
            {"id": "NK-FB-01", "name": "Sénégal Home 24/25", "genre": "Unisex", "sizes": ["M", "L", "XL", "XXL"], "price": 15000, "img": "https://images.unsplash.com/photo-1599408162161-08249033327d", "stock": "FLOCAGE DISPO"},
            {"id": "NK-BK-01", "name": "Maillot Basket USA Team", "genre": "Homme", "sizes": ["L", "XL", "XXL"], "price": 20000, "img": "https://images.unsplash.com/photo-1515523110800-9415d13b84a8", "stock": "DISPONIBLE"}
        ],
        "CHAUSSURES": [
            {"id": "NK-CH-01", "name": "Air Max Plus TN Requin", "genre": "Homme", "sizes": ["40", "41", "42", "43", "44"], "price": 85000, "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff", "stock": "PREMIUM"},
            {"id": "NK-CH-02", "name": "Nike Pegasus Running", "genre": "Femme", "sizes": ["37", "38", "39"], "price": 45000, "img": "https://images.unsplash.com/photo-1539185441755-769473a23570", "stock": "RUNNING"}
        ]
    },
    "ADIDAS": {
        "JOGGING": [
            {"id": "AD-JG-01", "name": "Ensemble Tiro 23 Pro", "genre": "Homme", "sizes": ["M", "L", "XL"], "price": 38000, "img": "https://images.unsplash.com/photo-1515444744559-7be63e1600de", "stock": "DISPONIBLE"}
        ],
        "CHAUSSURES": [
            {"id": "AD-CH-01", "name": "Adidas Predator Elite", "genre": "Homme", "sizes": ["41", "42", "43"], "price": 120000, "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2", "stock": "CRAMPONS"}
        ]
    },
    "MATÉRIEL & ACCESSOIRES": {
        "PROTECTION": [
            {"id": "ACC-01", "name": "Protège-tibias Carbon X", "genre": "Unisex", "sizes": ["S", "M", "L"], "price": 8500, "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca", "stock": "STOCK LIMITÉ"}
        ],
        "TEXTILE": [
            {"id": "ACC-02", "name": "Chaussettes Foot Elite", "genre": "Unisex", "sizes": ["39-42", "43-45"], "price": 4500, "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82", "stock": "DISPONIBLE"},
            {"id": "ACC-03", "name": "Dossarts Entraînement (Lot)", "genre": "Unisex", "sizes": ["Unique"], "price": 15000, "img": "https://images.unsplash.com/photo-1526401485004-46910ecc8e51", "stock": "PRO"}
        ]
    }
}

# --- 4. FILTRES DYNAMIQUES ---
with st.sidebar:
    st.markdown("<h2 style='color:#ffda00; font-family:Orbitron;'>AVENIR PANEL</h2>", unsafe_allow_html=True)
    sel_brand = st.selectbox("MARQUE", list(inventory.keys()))
    
    # Générer dynamiquement les sous-catégories selon la marque
    categories = list(inventory[sel_brand].keys())
    sel_cat = st.radio("CATÉGORIES", categories)
    
    st.divider()
    sel_genre = st.multiselect("GENRE", ["Homme", "Femme", "Unisex", "Enfant"], default=["Homme", "Femme", "Unisex"])
    
# --- 5. AFFICHAGE DES PRODUITS ---
st.markdown(f"""
    <div class="main-header">
        <h1 style="font-family:'Orbitron'; color:#ffda00; font-size:50px; margin:0;">AVENIR SPORT</h1>
        <p style="letter-spacing:10px;">SYSTEM : {sel_brand} // {sel_cat}</p>
    </div>
""", unsafe_allow_html=True)

items = inventory[sel_brand][sel_cat]
# Filtrage par genre
filtered_items = [i for i in items if i['genre'] in sel_genre]

if not filtered_items:
    st.warning("Aucun produit ne correspond à vos filtres.")
else:
    cols = st.columns(3)
    for idx, item in enumerate(filtered_items):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="brand-card">
                    <img src="{item['img']}" class="product-img">
                    <div style="padding:20px;">
                        <span class="status-badge" style="background:#ffda00; color:black;">{item['stock']}</span>
                        <p style="color:#666; font-size:11px; margin:0;">REF: {item['id']}</p>
                        <h3 style="margin:5px 0; font-family:'Inter';">{item['name']}</h3>
                        <p style="color:#888; font-size:12px;">Cible: {item['genre']}</p>
                        <div style="margin:15px 0;">
                            <small>TAILLES DISPONIBLES :</small><br>
                            {" ".join([f'<span class="size-box">{s}</span>' for s in item['sizes']])}
                        </div>
                        <div class="price-tag">{item['price']:,} FCFA</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("VÉRIFIER DISPONIBILITÉ", f"https://wa.me/221XXXXXXXXX?text=Bonjour, l'article {item['name']} (REF:{item['id']}) est-il disponible?")
            st.write("")

# --- 6. RÉSUMÉ GESTION ---
with st.expander("📝 RÉSUMÉ DES STOCKS POUR INVENTAIRE"):
    summary_data = []
    for brand, cats in inventory.items():
        for cat, prods in cats.items():
            for p in prods:
                summary_data.append({"Marque": brand, "Catégorie": cat, "Nom": p['name'], "Prix": p['price'], "Genre": p['genre']})
    st.table(pd.DataFrame(summary_data))
