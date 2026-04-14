import streamlit as st
import pandas as pd

# --- 1. CONFIGURATION SYSTÈME ---
st.set_page_config(
    page_title="AVENIR SPORT | ENTERPRISE RESOURCE PLANNING",
    page_icon="⚽",
    layout="wide"
)

# --- 2. CSS CUSTOM "INDUSTRIAL DARK" ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&display=swap');
    
    :root { --accent: #ffda00; --bg-main: #050505; --surface: #121212; }
    
    .stApp { background-color: var(--bg-main); color: #fff; }
    
    /* Global Container */
    .product-card {
        background: var(--surface);
        border: 1px solid #222;
        border-radius: 20px;
        padding: 0px;
        transition: 0.4s ease;
        height: 100%;
    }
    .product-card:hover { border-color: var(--accent); transform: translateY(-8px); }
    
    /* Badge System */
    .badge {
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 10px;
        font-weight: 800;
        text-transform: uppercase;
        margin-right: 5px;
    }
    .badge-brand { background: var(--accent); color: #000; }
    .badge-cat { background: #333; color: #fff; }
    
    /* Typography */
    .price-text { font-family: 'Orbitron'; font-size: 26px; color: var(--accent); font-weight: 900; }
    .model-title { font-family: 'Inter'; font-weight: 600; font-size: 20px; margin: 10px 0; }
    
    /* Size Grid */
    .size-grid { display: flex; flex-wrap: wrap; gap: 5px; margin: 15px 0; }
    .size-item {
        width: 40px; height: 30px; line-height: 30px; text-align: center;
        background: #000; border: 1px solid #333; font-size: 11px; border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ARCHITECTURE DE DONNÉES MASSIVE ---
class Product:
    def __init__(self, id, brand, category, model, genre, sizes, price, img, status="EN STOCK"):
        self.id = id
        self.brand = brand
        self.category = category
        self.model = model
        self.genre = genre
        self.sizes = sizes
        self.price = price
        self.img = img
        self.status = status

# Génération de la base de données (Exemple de structure extensible)
db = [
    # --- NIKE SECTION ---
    Product("NK-001", "NIKE", "JOGGING", "Tech Fleece Reborn", "Homme", ["S", "M", "L", "XL"], 45000, "https://i.ibb.co/gLjFBt4G/image.jpg"),
    Product("NK-002", "NIKE", "CRAMPONS", "Mercurial Superfly 9", "Unisex", ["40", "41", "42", "43", "44"], 135000, "https://i.ibb.co/RkYyxdkc/image.jpg", "ELITE"),
    Product("NK-SN-24", "NIKE", "MAILLOT FOOT", "Sénégal Home 24/25", "Unisex", ["M", "L", "XL", "XXL"], 15000, "https://i.ibb.co/bMShDsqb/image.jpg"),
    
    # --- ADIDAS SECTION ---
   Product("NK-003", "ADIDAS", "lIGHT", "ULTRABOOST", "Unisex", ["M", "L", "XL", "XXL"], 15000, "https://i.ibb.co/Tqh9ZW1j/image.jpg"),
    Product("AD-002", "ADIDAS", "JOGGING", "Tiro 23 Competition", "Homme", ["M", "L", "XL"], 38000,"https://i.ibb.co/Pszx1bRF/image.jpg"),
    
    # --- PUMA & NEW BALANCE ---
    Product("PM-001", "PUMA", "MAILLOT FOOT", "Man City Authentic", "Homme", ["S", "M", "L"], 18000, "https://i.ibb.co/ymGgtnCs/image.jpg"),
    Product("NB-001", "NEW BALANCE", "RUNNING", "Fresh Foam 1080", "Unisex", ["41", "42", "43", "44", "45"], 88000, "https://i.ibb.co/H3WtxHn/image.jpg"),
    
    # --- MATÉRIEL & ACCESSOIRES ---
    Product("ACC-01", "NIKE", "ACCESSOIRES", "Protège-Tibias Carbon", "Unisex", ["S", "M", "L"], 12000, "https://i.ibb.co/nsjnLfxv/image.jpg"),
    Product("ACC-02", "PUMA", "ACCESSOIRES", "Lot 10 Dossards Pro", "Unisex", ["Taille Unique"], 25000, "https://i.ibb.co/KpQ1Nmr5/image.jpg"),
    Product("ACC-03", "NIKE", "ACCESSOIRES", "Chaussettes Foot (Pack de 3)", "Unisex", ["38-42", "43-46"], 7500, "https://i.ibb.co/LDYs9CSt/image.jpg")
]

# --- 4. ENGINE DE FILTRAGE ---
with st.sidebar:
    st.markdown("### 🛠️ FILTRES AVANCÉS")
    search = st.text_input("RECHERCHE (Modèle, ID...)", placeholder="ex: Tech Fleece")
    
    st.divider()
    f_brand = st.multiselect("MARQUES", ["NIKE", "ADIDAS", "PUMA", "NEW BALANCE"], default=["NIKE", "ADIDAS", "PUMA", "NEW BALANCE"])
    f_cat = st.multiselect("CATÉGORIES", ["JOGGING", "MAILLOT FOOT", "CRAMPONS", "RUNNING", "ACCESSOIRES"], default=["JOGGING", "MAILLOT FOOT", "CRAMPONS", "RUNNING", "ACCESSOIRES"])
    f_genre = st.selectbox("GENRE CIBLE", ["Tous", "Homme", "Femme", "Unisex"])
    
    st.divider()
    price_range = st.slider("TRANCHE DE PRIX (FCFA)", 0, 200000, (0, 200000))

# Logique de filtrage
filtered_db = [
    p for p in db 
    if p.brand in f_brand 
    and p.category in f_cat
    and (f_genre == "Tous" or p.genre == f_genre)
    and (price_range[0] <= p.price <= price_range[1])
    and (search.lower() in p.model.lower() or search.lower() in p.id.lower())
]

# --- 5. INTERFACE D'AFFICHAGE ---
st.markdown(f"""
    <div style="text-align:center; padding:40px 0;">
        <h1 style="font-family:'Orbitron'; color:var(--accent); font-size:60px; letter-spacing:10px; margin:0;">AVENIR SPORT</h1>
        <p style="color:#666; letter-spacing:5px;">LOGISTICS & PERFORMANCE ERP v7.0</p>
    </div>
""", unsafe_allow_html=True)

# Affichage en grille
cols = st.columns(3)
for idx, p in enumerate(filtered_db):
    with cols[idx % 3]:
        sizes_html = "".join([f'<div class="size-item">{s}</div>' for s in p.sizes])
        st.markdown(f"""
            <div class="product-card">
                <img src="{p.img}" style="width:100%; height:300px; object-fit:cover; border-radius:20px 20px 0 0;">
                <div style="padding:20px;">
                    <div style="display:flex; justify-content:space-between;">
                        <div>
                            <span class="badge badge-brand">{p.brand}</span>
                            <span class="badge badge-cat">{p.category}</span>
                        </div>
                        <small style="color:#444;">{p.status}</small>
                    </div>
                    <h3 class="model-title">{p.model}</h3>
                    <p style="font-size:12px; color:#888;">Réf: {p.id} | Genre: {p.genre}</p>
                    <div class="size-grid">{sizes_html}</div>
                    <div class="price-text">{p.price:,} F</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("VÉRIFIER STOCK & COMMANDER", f"https://wa.me/221770953766?text=Bonjour, je souhaite commander la référence {p.id} ({p.model})")
        st.write("")

# --- 6. VUE ERP (ADMINISTRATION) ---
with st.expander("📊 ANALYSE DES STOCKS (MODE ADMIN)"):
    df = pd.DataFrame([vars(p) for p in db])
    st.dataframe(df, use_container_width=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Items", len(db))
    c2.metric("Valeur Stock", f"{sum(p.price for p in db):,} F")
    c3.metric("Marques", len(set(p.brand for p in db)))
    # --- 7. FOOTER MASSIVE ---
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
