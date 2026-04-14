
import streamlit as st

# Configuration
st.set_page_config(page_title="Avenir Sport Joal", page_icon="🏆")

# Titre
st.title("🦁 AVENIR SPORT JOAL")
st.subheader("Boutique officielle à Joal-Fadiouth")
st.write("---")

# Affichage des articles
col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/400x400.png?text=Maillot+Sénégal")
    st.write("### Maillot Sénégal")
    st.write("**Prix : 12 500 FCFA**")
    st.link_button("Commander via WhatsApp", "https://wa.me/221XXXXXXXXX")

with col2:
    st.image("https://via.placeholder.com/400x400.png?text=Chaussures+Sport")
    st.write("### Crampons Elite")
    st.write("**Prix : 25 000 FCFA**")
    st.link_button("Commander via WhatsApp", "https://wa.me/221XXXXXXXXX")

st.write("---")
st.write("© 2026 Avenir Sport Joal")
