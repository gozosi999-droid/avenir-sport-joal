import streamlit as st
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Avenir Sport Joal | Boutique Pro", layout="wide")

# --- DESIGN ULTRA PROFESSIONNEL (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

    /* Fond d'écran sombre avec image de stade */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=2000");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Titre Impact Sport */
    .titre-sport {
        font-family: 'Bebas Neue', cursive;
        font-size: clamp(50px, 8vw, 100px) !important;
        color: #ffda00; 
        text-align: center;
        text-transform: uppercase;
        font-style: italic;
        line-height: 1;
        text-shadow: 4px 4px 0px #000000;
        margin-bottom: 0px;
    }

    /* Sections Tracées */
    .section-header {
        border-left: 10px solid #ffda00;
        padding-left: 15px;
        color: white;
        font-family: 'Bebas Neue';
        font-size: 40px;
        margin-top: 40px;
        margin-bottom: 20px;
        background: rgba(255, 255, 255, 0.1);
    }

    /* Cartes Produits Premium */
    .product-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: black !important;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.5);
        margin-bottom: 25px;
    }

    .price-tag {
        background-color: #ffda00;
        color: black;
        font-weight: bold;
        font-size: 22px;
        padding: 5px 15px;
        border-radius: 5px;
        display: inline-block;
        margin: 10px 0;
    }

    /* Pied de page style City Sport */
    .footer {
        background-color: #000000;
        color: white;
        padding: 50px;
        margin-top: 80px;
        border-top: 4px solid #ffda00;
    }
    
    /* Boutons WhatsApp Verts */
    .stButton>button {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. EN-TÊTE
col_logo, col_titre = st.columns([1, 4])
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
with col_titre:
    st.markdown('<p class="titre-sport">AVENIR SPORT</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white; letter-spacing:3px;'>JOAL-FADIOUTH • SÉNÉGAL</p>", unsafe_allow_html=True)

st.write("---")

# 3. BARRE DE NAVIGATION (TABS)
tab1, tab2, tab3, tab4 = st.tabs(["🏠 ACCUEIL", "👕 MAILLOTS & HABITS", "👟 CHAUSSURES", "📞 NOUS CONTACTER"])

# --- SECTION ACCUEIL ---
with tab1:
    st.markdown('<div class="section-header">🔥 ARRIVAGES & PROMOS</div>', unsafe_allow_html=True)
    colA, colB = st.columns(2)
    with colA:
        st.image("https://images.unsplash.com/photo-1551854838-212c50b4c184?q=80&w=1000", caption="Nouveaux équipements arrivés de Dakar")
    with colB:
        st.markdown("<h2 style='color:white;'>Bienvenue chez le n°1 à Joal</h2>", unsafe_allow_html=True)
        st.write("Retrouvez les plus grandes marques et les meilleurs maillots Qualité Thaïlande.")
        st.button("Voir la collection complète")

# --- SECTION MAILLOTS & HABITS ---
with tab2:
    st.markdown('<div class="section-header">LES MAILLOTS (SAISON 2024/2025)</div>', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x300.png?text=Maillot+Sénégal")
        st.markdown("### MAILLOT SÉNÉGAL")
        st.markdown('<div class="price-tag">15.000 FCFA</div>', unsafe_allow_html=True)
        st.link_button("💬 COMMANDER", "https://wa.me/221XXXXXXXXX?text=Je%20veux%20le%20maillot%20Sénégal")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">VÊTEMENTS & SURVÊTEMENTS</div>', unsafe_allow_html=True)
    h1, h2, h3 = st.columns(3)
    # Ajoute ici tes habits...

# --- SECTION CHAUSSURES ---
with tab3:
    st.markdown('<div class="section-header">CHAUSSURES & CRAMPONS</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    # Ajoute ici tes chaussures...

# --- SECTION CONTACT (COORDONNÉES COMPLÈTES) ---
with tab4:
    st.markdown('<div class="section-header">CONTACTEZ LA BOUTIQUE</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style="background:rgba(255,255,255,0.1); padding:20px; border-radius:10px; color:white;">
        <h3>📍 ADRESSE PHYSIQUE</h3>
        <p>Avenir Sport Joal<br>Quartier Joal, Sénégal<br>(Près du terrain municipal)</p>
        <h3>📧 EMAIL PROFESSIONNEL</h3>
        <p>contact@avenirsportjoal.com</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.1); padding:20px; border-radius:10px; color:white;">
        <h3>📞 TÉLÉPHONE & WHATSAPP</h3>
        <p>Principal : +221 XX XXX XX XX</p>
        <p>Support : +221 XX XXX XX XX</p>
        <h3>📱 RÉSEAUX SOCIAUX</h3>
        <p>Instagram : @avenirsport_joal<br>Facebook : Avenir Sport Sénégal</p>
        </div>
        """, unsafe_allow_html=True)

# 4. FOOTER FINAL (STYLE CITY SPORT)
st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="min-width: 250px;">
                <h3 style="color:#ffda00;">AVENIR SPORT JOAL</h3>
                <p>La référence du sport au Sénégal.<br>Qualité Thaïlande & Authenticité.</p>
            </div>
            <div style="min-width: 250px;">
                <h3 style="color:#ffda00;">COORDONNÉES</h3>
                <p>📍 Joal, Sénégal</p>
                <p>📞 +221 XX XXX XX XX</p>
                <p>📧 contact@avenirsport.com</p>
            </div>
            <div style="min-width: 250px;">
                <h3 style="color:#ffda00;">HORAIRES</h3>
                <p>Lun - Sam : 09h - 21h</p>
                <p>Dimanche : 10h - 18h</p>
            </div>
        </div>
        <hr style="border-color: #333;">
        <p style="text-align: center; font-size: 14px; color: #888;">© 2026 Avenir Sport Joal - Site Officiel. Propulsé par Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)
