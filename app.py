
 import streamlit as st

# Configuration de la page avec un titre pro
st.set_page_config(page_title="Avenir Sport Joal | Officiel", page_icon="🏆", layout="wide")

# --- DESIGN PERSONNALISÉ (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ed1c24; /* Rouge Sport */
        color: white;
        font-weight: bold;
        border: none;
    }
    .product-box {
        border: 1px solid #333;
        padding: 20px;
        border-radius: 15px;
        background-color: #1d2129;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE DE NAVIGATION / EN-TÊTE ---
col_logo, col_text = st.columns([1, 4])
with col_text:
    st.title("🦁 AVENIR SPORT JOAL")
    st.write("📍 *Boutique officielle - Joal-Fadiouth, Sénégal*")

st.write("---")

# --- SECTION PROMOTIONS ---
st.warning("🔥 **ARRIVAGE DAKAR :** Nouveaux maillots Sénégal disponibles en boutique !")

# --- FILTRES DE RECHERCHE ---
cat = st.selectbox("Choisir une catégorie :", ["Tous nos articles", "Maillots", "Chaussures", "Accessoires"])

# --- GRILLE DE PRODUITS ---
st.subheader(f"Rayon : {cat}")
col1, col2, col3 = st.columns(3)

# Produit 1
with col1:
    st.markdown('<div class="product-box">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x400.png?text=Maillot+Senegal+2024", use_column_width=True)
    st.write("### Maillot Sénégal")
    st.write("⭐ Qualité Thaïlande AAA")
    st.write("💰 **12 500 FCFA**")
    st.success("✅ En Stock")
    st.link_button("Acheter sur WhatsApp", "https://wa.me/221XXXXXXXXX?text=Bonjour, je souhaite commander le maillot du Sénégal.")
    st.markdown('</div>', unsafe_allow_html=True)

# Produit 2
with col2:
    st.markdown('<div class="product-box">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x400.png?text=Crampons+Elite", use_column_width=True)
    st.write("### Crampons Nike Elite")
    st.write("⭐ Performance Pro")
    st.write("💰 **25 000 FCFA**")
    st.success("✅ En Stock")
    st.link_button("Acheter sur WhatsApp", "https://wa.me/221770953766?text=Bonjour, je souhaite commander les crampons.")
    st.markdown('</div>', unsafe_allow_html=True)

# Produit 3
with col3:
    st.markdown('<div class="product-box">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x400.png?text=Ballon+Ligue+1", use_column_width=True)
    st.write("### Ballon Officiel")
    st.write("⭐ Qualité Hybride")
    st.write("💰 **10 000 FCFA**")
    st.error("⌛ Rupture de stock")
    st.link_button("M'avertir du retour", "https://wa.me/221769038755?text=Prévenez-moi pour le ballon.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PIED DE PAGE ---
st.write("---")
st.write("© 2024 Avenir Sport Joal. Design by Gemini.")
