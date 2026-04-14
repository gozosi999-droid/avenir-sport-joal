import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Avenir Sport Joal", page_icon="⚽")

# --- TITRE ET ENTÊTE ---
st.title("🦁 AVENIR SPORT JOAL")
st.write("### L'excellence au service du sport à Joal")
st.write("---")

# --- CATALOGUE ---
st.header("Nos Articles")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Maillot Sénégal")
    st.write("Qualité Thaïlande AAA")
    st.write("**Prix : 12 000 FCFA**")
    # Remplace le numéro par le tien pour que ça marche !
    st.link_button("Réserver sur WhatsApp", "https://wa.me/221XXXXXXXXX?text=Je%20veux%20le%20maillot%20du%20Sénégal")

with col2:
    st.subheader("Crampons Foot")
    st.write("Nike / Adidas - Qualité A")
    st.write("**Prix : 25 000 FCFA**")
    st.link_button("Réserver sur WhatsApp", "https://wa.me/221XXXXXXXXX?text=Je%20veux%20les%20crampons")

# --- INFOS BOUTIQUE ---
st.write("---")
st.info("📍 Notre boutique se trouve à Joal-Fadiouth. Local propre de 18m².")
