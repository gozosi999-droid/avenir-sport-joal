import streamlit as st
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Avenir Sport Joal | Boutique Officielle", layout="wide")

# --- STYLE CSS AVANCÉ ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
    
    .stApp {
        background-color: #f4f4f4; /* Fond gris très clair pour faire ressortir les produits */
    }
    
    .titre-sport {
        font-family: 'Bebas Neue', cursive;
        font-size: 80px !important;
        color: #000000;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .section-header {
        background-color: #000000;
        color: #ffda00;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-family: 'Bebas Neue';
        font-size: 30px;
        margin-top: 50px;
    }
    
    .product-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        text-align: center;
        transition: 0.3s;
    }
    
    .footer {
        background-color: #1a1a1a;
        color: white;
        padding: 40px;
        margin-top: 100px;
        border-top: 5px solid #ffda00;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. EN-TÊTE (LOGO & NOM)
col_logo, col_titre = st.columns([1, 4])
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
with col_titre:
    st.markdown('<p class="titre-sport">AVENIR SPORT JOAL</p>', unsafe_allow_html=True)

# 3. NAVIGATION PAR SECTIONS
st.write("---")
menu = ["🏠 Accueil", "👕 Maillots", "👟 Chaussures", "🎒 Accessoires", "📞 Contact"]
choix = st.tabs(menu)

# --- SECTION ACCUEIL ---
with choix[0]:
    st.image("https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?q=80&w=2000", caption="Nouvelle Collection 2026")
    st.markdown("## 🔥 Nos Meilleures Ventes")
    # Ici tu peux mettre un mélange de tout

# --- SECTION MAILLOTS ---
with choix[1]:
    st.markdown('<div class="section-header">RAYON MAILLOTS OFFICIELS</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x300.png?text=Senegal+Home")
        st.write("### Maillot Sénégal Home")
        st.markdown("**15 000 FCFA**")
        st.link_button("WhatsApp 💬", "https://wa.me/221XXXXXXXXX")
        st.markdown('</div>', unsafe_allow_html=True)
    # Ajouter d'autres maillots ici...

# --- SECTION CHAUSSURES ---
with choix[2]:
    st.markdown('<div class="section-header">CHAUSSURES & CRAMPONS</div>', unsafe_allow_html=True)
    # Même structure que les maillots

# --- SECTION CONTACT & COORDONNÉES ---
with choix[4]:
    st.markdown("## 📍 Nos Coordonnées")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("""
        **📍 ADRESSE :** Joal-Fadiouth, Sénégal  
        À côté du terrain de sport.
        """)
    with col_b:
        st.success(f"""
        **📞 CONTACTS :** **Téléphone :** +221 XX XXX XX XX  
        **Email :** ton-email@gmail.com  
        **WhatsApp :** [Cliquez ici pour discuter](https://wa.me/221XXXXXXXXX)
        """)

# 4. LE PIED DE PAGE (FOOTER PROFESSIONNEL)
st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: space-around;">
            <div>
                <h4>AVENIR SPORT JOAL</h4>
                <p>Qualité Premium au meilleur prix.</p>
            </div>
            <div>
                <h4>LIENS UTILES</h4>
                <p>• Instagram : @avenirsportjoal</p>
                <p>• Facebook : Avenir Sport</p>
            </div>
            <div>
                <h4>SERVICE CLIENT</h4>
                <p>📞 +221 XX XXX XX XX</p>
                <p>📧 contact@avenirsport.com</p>
            </div>
        </div>
        <hr style='border: 1px solid #444'>
        <p style='text-align: center;'>© 2026 Avenir Sport Joal. Tous droits réservés.</p>
    </div>
    """, unsafe_allow_html=True)
