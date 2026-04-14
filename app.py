import streamlit as st
import os

# 1. CONFIGURATION
st.set_page_config(page_title="Avenir Sport Joal | Officiel", layout="wide")

# --- STYLE CSS AVANCÉ (Motifs et Couleurs Premium) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@300;400;700&display=swap');

    /* Fond avec voile sombre pour faire ressortir le design */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url("https://images.unsplash.com/photo-1551952237-954a0e68786c?q=80&w=2000");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Titre Impact Sport */
    .titre-sport {
        font-family: 'Bebas Neue', cursive;
        font-size: 90px !important;
        color: #ffda00; 
        text-align: center;
        text-transform: uppercase;
        font-style: italic;
        line-height: 0.9;
        text-shadow: 5px 5px 0px #000000;
        margin-bottom: 5px;
    }

    /* Design des Sections "Tracées" */
    .section-divider {
        border-bottom: 4px solid #ffda00;
        width: 100px;
        margin: 10px auto 30px auto;
    }

    .rayon-title {
        font-family: 'Bebas Neue';
        font-size: 45px;
        color: white;
        background: rgba(255, 218, 0, 0.1);
        padding: 10px 20px;
        border-left: 8px solid #ffda00;
        margin-top: 30px;
    }

    /* Cartes Produits Professionnelles */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: #1a1a1a !important;
        box-shadow: 0px 15px 30px rgba(0,0,0,0.5);
        transition: transform 0.3s ease;
    }
    .product-card:hover {
        transform: translateY(-10px); /* Animation au survol */
    }

    .price-tag {
        background-color: #ffda00;
        color: black;
        font-weight: bold;
        font-size: 24px;
        padding: 5px 20px;
        border-radius: 50px;
        display: inline-block;
        margin: 15px 0;
    }

    /* Pied de Page Noir Profond */
    .footer-container {
        background-color: #000000;
        color: white;
        padding: 60px 20px;
        margin-top: 100px;
        border-top: 6px solid #ffda00;
        font-family: 'Roboto', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. HEADER
col_l, col_r = st.columns([1, 4])
with col_l:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
with col_r:
    st.markdown('<p class="titre-sport">AVENIR SPORT</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white; letter-spacing:8px; font-weight:bold;'>JOAL-FADIOUTH • SÉNÉGAL</p>", unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 3. SYSTÈME DE NAVIGATION PAR ONGLETS
tabs = st.tabs(["🏠 ACCUEIL", "👕 MAILLOTS & HABITS", "👟 CHAUSSURES", "📞 NOUS CONTACTER"])

# --- ONGLET 1 : ACCUEIL ---
with tabs[0]:
    st.markdown("<h2 style='color:white; text-align:center;'>DÉCOUVREZ LA NOUVELLE COLLECTION</h2>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=2000", use_container_width=True)
    st.write("")
    col_feat1, col_feat2 = st.columns(2)
    with col_feat1:
        st.info("🚛 **Livraison Rapide** sur Joal et Dakar.")
    with col_feat2:
        st.success("💎 **Qualité Premium** garantie (Thaïlande AAA).")

# --- ONGLET 2 : MAILLOTS & HABITS ---
with tabs[1]:
    st.markdown('<div class="rayon-title">MAILLOTS NATIONAUX & CLUBS</div>', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x400.png?text=Maillot+Senegal")
        st.markdown("### MAILLOT SÉNÉGAL 2024")
        st.markdown('<div class="price-tag">15.000 F</div>', unsafe_allow_html=True)
        st.link_button("COMMANDER SUR WHATSAPP", "https://wa.me/221XXXXXXXXX")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="rayon-title">HABITS & SURVÊTEMENTS</div>', unsafe_allow_html=True)
    # Espace pour tes ensembles, survêtements et t-shirts

# --- ONGLET 3 : CHAUSSURES ---
with tabs[2]:
    st.markdown('<div class="rayon-title">CHAUSSURES & CRAMPONS</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x400.png?text=Nike+Vapor")
        st.markdown("### NIKE VAPOR ELITE")
        st.markdown('<div class="price-tag">35.000 F</div>', unsafe_allow_html=True)
        st.link_button("COMMANDER SUR WHATSAPP", "https://wa.me/221XXXXXXXXX")
        st.markdown('</div>', unsafe_allow_html=True)

# --- ONGLET 4 : CONTACT ---
with tabs[3]:
    st.markdown('<div class="rayon-title">NOS COORDONNÉES</div>', unsafe_allow_html=True)
    c_info, c_map = st.columns(2)
    with c_info:
        st.markdown("""
        <div style="color:white; font-size:18px;">
        <p><strong>📞 TÉLÉPHONE :</strong> +221 77 XXX XX XX</p>
        <p><strong>📧 EMAIL :</strong> avenirsportjoal@gmail.com</p>
        <p><strong>📍 ADRESSE :</strong> Joal-Fadiouth, Quartier Escale</p>
        <p><strong>🕒 HORAIRES :</strong> 09:00 - 22:00 (7j/7)</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("DISCUTER SUR WHATSAPP MAINTENANT", "https://wa.me/221XXXXXXXXX")

# 4. FOOTER (PIED DE PAGE)
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="min-width: 200px; margin-bottom: 20px;">
                <h3 style="color:#ffda00;">AVENIR SPORT</h3>
                <p>La puissance du sport à Joal.</p>
            </div>
            <div style="min-width: 200px; margin-bottom: 20px;">
                <h4 style="color:#ffda00;">RAYONS</h4>
                <p>• Maillots<br>• Chaussures<br>• Accessoires</p>
            </div>
            <div style="min-width: 200px; margin-bottom: 20px;">
                <h4 style="color:#ffda00;">SUIVEZ-NOUS</h4>
                <p>Instagram : @avenirsport_joal<br>Facebook : Avenir Sport Joal</p>
            </div>
        </div>
        <p style="text-align:center; font-size:12px; margin-top:50px; opacity:0.5;">
        © 2026 AVENIR SPORT JOAL - Boutique de sport officielle à Joal-Fadiouth, Sénégal.
        </p>
    </div>
    """, unsafe_allow_html=True)
