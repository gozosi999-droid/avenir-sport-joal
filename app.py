import streamlit as st
import os

# 1. CONFIGURATION
st.set_page_config(page_title="Avenir Sport Joal | Officiel", layout="wide")

# --- DESIGN CSS SUR MESURE (Oublie les onglets gris !) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)), 
                    url("https://images.unsplash.com/photo-1510051646653-c33c209f9880?q=80&w=2000");
        background-size: cover;
    }

    /* TITRE PHÉNOMÉNAL */
    .titre-sport {
        font-family: 'Bebas Neue';
        font-size: 100px !important;
        color: #ffda00;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 5px;
        margin-bottom: 0px;
        text-shadow: 0px 10px 20px rgba(255, 218, 0, 0.3);
    }

    /* NAVIGATION VISUELLE (LES CARTES) */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 50px 0;
    }

    .nav-card {
        background: rgba(255, 218, 0, 0.1);
        border: 2px solid #ffda00;
        border-radius: 15px;
        padding: 30px;
        width: 200px;
        text-align: center;
        transition: 0.4s;
        cursor: pointer;
        text-decoration: none !important;
    }

    .nav-card:hover {
        background: #ffda00;
        transform: translateY(-10px);
        box-shadow: 0px 0px 30px #ffda00;
    }

    .nav-card h2 {
        font-family: 'Bebas Neue' !important;
        font-size: 30px !important;
        color: white;
        margin: 0;
    }

    .nav-card:hover h2 {
        color: black !important;
    }

    /* PRODUITS */
    .product-box {
        background: white;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        color: black !important;
        border-bottom: 5px solid #ffda00;
    }
    
    .price {
        font-family: 'Bebas Neue';
        font-size: 28px;
        color: #e60000;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGO ET TITRE
st.markdown('<p class="titre-sport">AVENIR SPORT</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; opacity:0.6; letter-spacing:5px;'>JOAL-FADIOUTH SÉNÉGAL</p>", unsafe_allow_html=True)

# 3. NOUVELLE NAVIGATION (SÉLECTEUR)
# Au lieu d'onglets, on utilise un bouton radio stylé ou un sélecteur propre
st.write("")
choix = st.selectbox("", ["🏠 ACCUEIL", "👕 MAILLOTS OFFICIELS", "👟 CHAUSSURES DE LUXE", "📞 CONTACT & INFOS"])

# --- CONTENU DYNAMIQUE ---

if "🏠 ACCUEIL" in choix:
    st.markdown("<h1 style='color:white; text-align:center;'>ARRIVAGES DE LA SEMAINE</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1543326727-cf6c39e8f84c?q=80&w=2000")
    
elif "👕 MAILLOTS" in choix:
    st.markdown("<h1 style='color:white; border-left: 10px solid #ffda00; padding-left:20px;'>MAILLOTS THAÏLANDE AAA</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    # Exemple d'article
    with col1:
        st.markdown("""
            <div class="product-box">
                <img src="https://images.unsplash.com/photo-1599408162161-08249033327d?w=400" style="width:100%; border-radius:10px;">
                <h2 style="color:black;">MAILLOT SÉNÉGAL</h2>
                <p class="price">15.000 FCFA</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("ACHETER MAINTENANT", "https://wa.me/221XXXXXXXXX")

elif "👟 CHAUSSURES" in choix:
    st.markdown("<h1 style='color:white; border-left: 10px solid #ffda00; padding-left:20px;'>CRAMPONS & BASKETS</h1>", unsafe_allow_html=True)
    # Structure identique pour les chaussures

elif "📞 CONTACT" in choix:
    st.markdown("<h1 style='color:white; text-align:center;'>REJOIGNEZ LA TEAM</h1>", unsafe_allow_html=True)
    st.info("📍 Joal, Quartier Escale | 📞 +221 77 XXX XX XX")

# 4. FOOTER (EXTRÊMEMENT LONG)
st.markdown("""
    <div style="background:black; color:gray; padding:100px 50px; margin-top:100px; border-top:1px solid #333;">
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:50px;">
            <div>
                <h3 style="color:#ffda00;">AVENIR SPORT</h3>
                <p>Le plus grand choix d'articles de sport à Joal-Fadiouth. Nous importons les meilleures qualités pour les champions.</p>
            </div>
            <div>
                <h3 style="color:#ffda00;">HORAIRES</h3>
                <p>Lundi - Samedi : 09h00 - 22h00<br>Dimanche : 10h00 - 18h00</p>
            </div>
            <div>
                <h3 style="color:#ffda00;">PAIEMENT</h3>
                <p>Wave<br>Orange Money<br>Espèces</p>
            </div>
            <div>
                <h3 style="color:#ffda00;">RÉSEAUX</h3>
                <p>Instagram<br>TikTok<br>Facebook</p>
            </div>
        </div>
        <p style="text-align:center; margin-top:50px;">© 2026 AVENIR SPORT JOAL - Excellence Sportive</p>
    </div>
""", unsafe_allow_html=True)
